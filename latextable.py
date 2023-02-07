"""
Drawing functions for outputting a Texttable table in a Latex format.
"""
import texttable


class DropColumnError(Exception):

    def __init__(self, column, header):
        super().__init__("Cannot drop column {:s} - column not in table header ({:s})\n".format(column, str(header)))


class DropRowError(Exception):

    def __init__(self, n_rows, row_idx):
        super().__init__("Cannot drop row {:d} - row is outside the range [1,{:d}]\n".format(row_idx, n_rows))


def draw_latex(table, caption=None, caption_short=None, caption_above=False, label=None, drop_columns=None,
               drop_rows=None, position=None, use_booktabs=False):
    """
    Draw a Texttable table in Latex format.
    Aside from table, all arguments are optional.

    :param table: Texttable table to be rendered in Latex, or a list of rows that represents a table.
    :param caption: A string that adds a caption to the Latex formatting.
    :param caption_short: A string that adds a short caption (used in the list of tables). Ignored if caption is None.
    :param caption_above: If True, the caption will be added above the table rather than below it (default).
    :param label: A string that adds a referencing label to the Latex formatting.
    :param drop_columns: A list of column names that won't be in the Latex output.
            Each column name must be in the table header.
    :param drop_rows: A list of row indices that won't be in the Latex output.
            Each row index must be in [0, number of rows - 1], where number of rows does not include the header.
    :param position: A string that represents LaTex's float position of the table.
            For example 'ht' results in the float position [ht].
    :param use_booktabs: Whether to override the table formatting with booktabs (https://ctan.org/pkg/booktabs?lang=en).
            If true, the texttable formatting is ignored, and instead the default booktabs style is used.
            This overrides the border, vertical lines, and horizontal lines.
            Note the booktabs package will need to be included in your Latex document (\\usepackage{booktabs}).
            Defaults to false.

    :return: The formatted Latex table returned as a single string.
    """
    # If passed a list of rows rather than a table, create the table first
    if type(table) != texttable.Texttable:
        rows = table
        table = texttable.Texttable()
        table.add_rows(rows)

    # Sanitise inputs
    _sanitise_drop_columns(table._header, drop_columns)
    _sanitise_drop_rows(len(table._rows), drop_rows)

    # Create and return the latex output
    out = ""
    out += _draw_latex_preamble(table=table,
                                position=position,
                                caption=caption if caption_above else None,
                                caption_short=caption_short if caption_above else None,
                                use_booktabs=use_booktabs)
    out += _draw_latex_header(table=table,
                              drop_columns=drop_columns,
                              use_booktabs=use_booktabs)
    out += _draw_latex_content(table=table,
                               drop_columns=drop_columns,
                               drop_rows=drop_rows,
                               use_booktabs=use_booktabs)
    out += _draw_latex_postamble(table=table,
                                 caption=caption if not caption_above else None,
                                 caption_short=caption_short if not caption_above else None,
                                 label=label,
                                 use_booktabs=use_booktabs)
    return out


def _draw_latex_preamble(table, position, caption, caption_short, use_booktabs):
    """
    Draw the Latex table preamble.

    Applies column horizontal alignment
    Applies columns vlines and table vertical border if appropriate.

    Example Output:
        \begin{table}
            \begin{center}
                \begin{tabular}{|l|r|c|}

    :param table: Texttable table to be rendered in Latex.
    :return: The Latex table preamble as a single string.
    """
    # Start table with optional position
    out = "\\begin{table}"
    if position is not None:
        out += '[{}]'.format(position)
    out += "\n"

    # Add caption if given
    out += _draw_table_caption(caption, caption_short)

    # Begin center
    out += _indent_text("\\begin{center}\n", 1)

    # Column setup with/without vlines
    #  If texttable align not set, default to left alignment (as per texttable)
    if not hasattr(table, "_align"):
        table._align = ["l"] * table._row_size
    if table._has_vlines() and not use_booktabs:
        column_str = "|".join(table._align)
    else:
        column_str = "".join(table._align)

    # Border with/without edges
    if table._has_border() and not use_booktabs:
        tabular_str = "\\begin{tabular}{|" + column_str + "|}\n"
    else:
        tabular_str = "\\begin{tabular}{" + column_str + "}\n"
    out += _indent_text(tabular_str, 2)

    return out


def _draw_latex_header(table, drop_columns, use_booktabs):
    """
    Draw the Latex header.

    Applies header border if appropriate.

    Example Output:
        \hline
        Name & Age & Nickname \\
        \hline

    :param table: Texttable table to be rendered in Latex.
    :param drop_columns: A list of columns that should not be in the final Latex output.
    :return: The Latex table header as a single string.
    """
    out = ""
    if table._has_border() or use_booktabs:
        rule = 'toprule' if use_booktabs else 'hline'
        out += _indent_text("\\{}\n".format(rule), 3)

    # Drop header columns if required
    header = _drop_columns(table._header.copy(), table._header, drop_columns)
    out += _indent_text(" & ".join(header) + " \\\\\n", 3)

    if table._has_header() or use_booktabs:
        rule = 'midrule' if use_booktabs else 'hline'
        out += _indent_text("\\{}\n".format(rule), 3)
    return out


def _draw_latex_content(table, drop_columns, drop_rows, use_booktabs):
    """
    Draw the Latex table content.

    Example Output:
        MrXavierHuon & 32 & Xav' \\
        \hline
        MrBaptisteClement & 1 & Baby \\
        \hline
        MmeLouiseBourgeau & 28 & Lou Loue \\

    :param table: Texttable table to be rendered in Latex.
    :param drop_columns: A list of columns that should not be in the final Latex output.
    :param drop_columns: A list of row indices that should not be in the final Latex output.
    :return: The Latex table content as a single string.
    """
    out = ""
    rows = _drop_rows(table._rows, drop_rows)
    for idx, row in enumerate(rows):
        row = _drop_columns(row, table._header, drop_columns)
        clean_row = _clean_row(row)
        out += _indent_text(" & ".join(clean_row) + " \\\\\n", 3)
        if table._has_hlines() and idx != len(table._rows) - 1 and not use_booktabs:
            out += _indent_text("\\hline\n", 3)
    return out


def _draw_latex_postamble(table, caption, caption_short, label, use_booktabs):
    """
    Draw the Latex table postamble.

    Adds caption and label if given.
    Applies table bottom border if appropriate.

    Example Output:
            \hline
            \end{tabular}
        \end{center}
        \caption{An example table.}
        \label{table:example_table}
    \end{table}

    :param table: Texttable table to be rendered in Latex.
    :param caption: A caption to add to the table.
    :param caption_short: Short caption used in the list of tables. Ignored if caption is None.
    :param label: A label to add to the table.
    :return: The Latex table postamble as one string.
    """
    # Add bottom rule
    out = ""
    if table._has_border() or use_booktabs:
        rule = 'bottomrule' if use_booktabs else 'hline'
        out += _indent_text("\\{}\n".format(rule), 3)

    # Close tabular and center environments
    out += _indent_text("\\end{tabular}\n", 2)
    out += _indent_text("\\end{center}\n", 1)

    # Add caption if given
    out += _draw_table_caption(caption, caption_short)

    # Add caption if given
    if label is not None:
        out += _indent_text("\\label{" + label + "}\n", 1)

    # End!
    out += "\\end{table}"
    return out


def _draw_table_caption(caption, caption_short):
    out = ""
    if caption is not None:
        out += _indent_text("\\caption", 1)
        if caption_short is not None:
            out += "[" + caption_short + "]"
        out += "{" + caption + "}\n"
    return out


def _clean_row(row):
    """
    Clean a row prior to drawing. Currently just removes newlines.

    :param row: Row to clean.
    :return: Cleaned row.
    """
    clean_row = []
    for element in row:
        clean_row.append(element.replace("\n", ""))
    return clean_row


def _sanitise_drop_columns(header, drop_columns):
    """
    Check the columns to be dropped - each column must be in the table header.

    :param header: Table header array.
    :param drop_columns: List of columns to be dropped.
    :return: None
    """
    if drop_columns is None:
        return
    # Check columns (ignores case).
    for column in drop_columns:
        if column.upper() not in [h.upper() for h in header]:
            raise DropColumnError(column, header)


def _drop_columns(target, header, drop_columns):
    """
    Drop columns from a target array.

    :param target: Array from which the columns should be dropped.
    :param header: Table header array.
    :param drop_columns: The columns that should be dropped. Each column should be in the header.
    :return: The target array with the relevant columns dropped.
    """
    target = target[:]
    if drop_columns is None:
        return target
    # Get indices to delete
    to_delete = []
    for column in drop_columns:
        column_idx = header.index(column)
        to_delete.append(column_idx)
    # Delete relevant indices (in reverse order so deletion doesn't affect other index positions)
    for i in sorted(to_delete, reverse=True):
        del target[i]
    return target


def _sanitise_drop_rows(n_rows, drop_rows):
    """
    Check the rows to be dropped - 0 <= row_idx < n_rows for each row_idx to be dropped.

    :param drop_rows: List of rows to be dropped.
    :param n_rows: Number of rows in the table (excluding the header).
    :return: None
    """
    if drop_rows is None:
        return
    # Check row idxs (ignores case).
    for row_idx in drop_rows:
        if not 0 <= row_idx < n_rows:
            raise DropRowError(n_rows, row_idx)


def _drop_rows(rows, drop_rows):
    """
    Drop rows by their indices.

    :param rows: Table from which the rows should be dropped.
    :param drop_rows: List of rows to be dropped.
    :return: The target array with the relevant rows dropped.
    """
    rows = rows[:]
    if drop_rows is None:
        return rows
    # Delete relevant indices (in reverse order so deletion doesn't affect other index positions)
    for i in sorted(drop_rows, reverse=True):
        del rows[i]
    return rows


def _indent_text(text, indent):
    """
    Indent a string by a certain number of tabs.

    :param text: String to indent.
    :param indent: Number of tabs.
    :return: The indented string.
    """
    return '\t' * indent + text
