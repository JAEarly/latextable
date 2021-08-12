"""
Drawing functions for outputting a Texttable table in a Latex format.
"""


class DropColumnError(Exception):

    def __init__(self, column, header):
        super().__init__("Cannot drop column {:s} - column not in table header ({:s})\n".format(column, str(header)))


def draw_latex(table, caption=None, label=None, drop_columns=None, position=None, use_booktabs=False):
    """
    Draw a Texttable table in Latex format.
    Aside from table, all arguments are optional.

    :param table: Texttable table to be rendered in Latex.
    :param caption: A string that adds a caption to the Latex formatting.
    :param label: A string that adds a referencing label to the Latex formatting.
    :param drop_columns: A list of column names that won't be in the Latex output.
            Each column name must be in the table header.
    :param position: A string that represents LaTex's float position of the table.
            For example 'ht' results in the float position [ht].
    :param use_booktabs: Whether to override the table formatting with booktabs (https://ctan.org/pkg/booktabs?lang=en).
            If true, the texttable formatting is ignored, and instead the default booktabs style is used.
            This overrides the border, vertical lines, and horizontal lines.
            Note the booktabs package will need to be included in your Latex document (\\usepackage{booktabs}).
            Defaults to false.
    :return: The formatted Latex table returned as a single string.
    """
    _sanitise_drop_columns(table._header, drop_columns)
    out = ""
    out += _draw_latex_preamble(table, position, use_booktabs)
    out += _draw_latex_header(table, drop_columns, use_booktabs)
    out += _draw_latex_content(table, drop_columns)
    out += _draw_latex_postamble(table, caption, label, use_booktabs)
    return out


def _draw_latex_preamble(table, position, use_booktabs):
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
    out = "\\begin{table}" 

    if position is not None:
        out += '[{}]'.format(position)

    out += "\n"
    out += _indent_text("\\begin{center}\n", 1)

    # Column setup with/without vlines
    if table._has_vlines() and not use_booktabs:
        column_str = "|".join(table._align)
    else:
        column_str = " ".join(table._align)

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


def _draw_latex_content(table, drop_columns):
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
    :return: The Latex table content as a single string.
    """
    out = ""
    for idx, row in enumerate(table._rows):
        row = _drop_columns(row, table._header, drop_columns)
        clean_row = _clean_row(row)
        out += _indent_text(" & ".join(clean_row) + " \\\\\n", 3)
        if table._has_hlines() and idx != len(table._rows) - 1:
            out += _indent_text("\\hline\n", 3)
    return out


def _draw_latex_postamble(table, caption, label, use_booktabs):
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
    :param label: A label to add to the table.
    :return: The Latex table postamble as one string.
    """
    out = ""
    if table._has_border() or use_booktabs:
        rule = 'bottomrule' if use_booktabs else 'hline'
        out += _indent_text("\\{}\n".format(rule), 3)
    out += _indent_text("\\end{tabular}\n", 2)
    out += _indent_text("\\end{center}\n", 1)
    if caption is not None:
        out += _indent_text("\\caption{" + caption + "}\n", 1)
    if label is not None:
        out += _indent_text("\\label{" + label + "}\n", 1)
    out += "\\end{table}"
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


def _indent_text(text, indent):
    """
    Indent a string by a certain number of tabs.

    :param text: String to indent.
    :param indent: Number of tabs.
    :return: The indented string.
    """
    return '\t' * indent + text
