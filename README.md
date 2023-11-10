# latextable

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Build Status](https://github.com/JAEarly/latextable/workflows/build/badge.svg)
[![Downloads](https://static.pepy.tech/personalized-badge/latextable?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/latextable)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/JosephAEarly?country.x=GB&locale.x=en_GB)

<p align="center">
	<img src="/docs/latextable_logo.png" width="300" />
</p>

[Texttable](https://github.com/foutaise/texttable) is a Python package that can create simple ASCII tables.
This package extends its functionality to allow the table to be directly output in Latex, removing the tedious copy and paste chore.
The Latex output matches the table design, and there are utilities for adding table captions, labels, and positions.

## Features
- Draw a table object in a Latex format.
- Matches table decoration (border, header, hlines, vlines).
- Applies horizontal column alignment.
- Allows the user to drop columns and rows from the output.
- Provides the ability to add a caption, reference label, and position to the Latex output.
- The output is correctly indented for directly copying into Latex.
- Supports [booktabs](https://ctan.org/pkg/booktabs?lang=en) formatting.
- Multicolumn headers can be included.
- Table data can be aliased for Latex output (e.g., escaping characters).

## Installation

PyPi:

```
pip install latextable
```

Requirements:

```
texttable
```

## Usage

The single function `latextable.draw_latex` returns a formatted Latex string based on the provided Texttable table or rows.
Aside from table, all arguments are optional.
Full documentation is available on [Read the Docs](https://latextable.readthedocs.io/en/latest/).

```
def draw_latex(table, caption=None, caption_short=None, caption_above=False, label=None, drop_columns=None,
               drop_rows=None, position=None, use_booktabs=False, multicolumn_header=None, alias=None):
    table: Texttable table to be rendered in Latex, or a list of rows that represents a table.
    caption: A string that adds a caption to the Latex formatting.
    caption_short: A string that adds a short caption (used in the list of tables). Ignored if caption is None.
    caption_above: If True, the caption will be added above the table rather than below it (default).
    label: A string that adds a referencing label to the Latex formatting.
    drop_columns: A list of column names that won't be in the Latex output.
     Each column name must be in the table header.
    drop_rows: A list of row indices that won't be in the Latex output.
     Each row index must be in [0, number of rows - 1], where number of rows does not include the header.
    position: A string that represents LaTex's float position of the table.
     For example 'ht' results in the float position [ht].
    use_booktabs: Whether to override the table formatting with booktabs (https://ctan.org/pkg/booktabs?lang=en).
     If true, the texttable formatting is ignored, and instead the default booktabs style is used.
     This overrides the border, vertical lines, and horizontal lines.
     Note the booktabs package will need to be included in your Latex document (\\usepackage{booktabs}).
     Defaults to false.
    multicolumn_header: A list of 2-tuples that defines multicolumn header names and widths.
     An additional header row will be added above the normal header row.
     The first entry in each 2-tuple is the header name, and the second entry is the number of columns it spans.
     The sum of column widths should equal the number of columns (after dropping any requested columns).
    alias: A str -> str dictionary denoting strings in the table data that should be aliased in the Latex output.
     Useful for escaping special Latex characters (e.g. &) or inserting custom Latex.
     For example, to replace '+-' with '$\\pm$', the dict would be {'+-': '$\\pm$'}.

    return: The formatted Latex table returned as a single string.
```

### Examples
A basic example is given below.
For more see the [examples directory](examples).

Code:

```
table_1 = Texttable()
table_1.set_cols_align(["l", "r", "c"])
table_1.set_cols_valign(["t", "m", "b"])
table_1.add_rows([["Name", "Age", "Nickname"],
                 ["Mr\nXavier\nHuon", 32, "Xav'"],
                 ["Mr\nBaptiste\nClement", 1, "Baby"],
                 ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"]])
print('-- Example 1: Basic --')
print('Texttable Output:')
print(table_1.draw())
print('\nLatextable Output:')
print(latextable.draw_latex(table_1, caption="An example table.", label="table:example_table"))
```

Output:

```
-- Example 1: Basic --
Texttable Output:
+----------+-----+----------+
|   Name   | Age | Nickname |
+==========+=====+==========+
| Mr       |     |          |
| Xavier   |  32 |          |
| Huon     |     |   Xav'   |
+----------+-----+----------+
| Mr       |     |          |
| Baptiste |   1 |          |
| Clement  |     |   Baby   |
+----------+-----+----------+
| Mme      |     |   Lou    |
| Louise   |  28 |          |
| Bourgeau |     |   Loue   |
+----------+-----+----------+

Latextable Output:
\begin{table}
	\begin{center}
		\begin{tabular}{|l|r|c|}
			\hline
			Name & Age & Nickname \\
			\hline
			MrXavierHuon & 32 & Xav' \\
			\hline
			MrBaptisteClement & 1 & Baby \\
			\hline
			MmeLouiseBourgeau & 28 & Lou Loue \\
			\hline
		\end{tabular}
	\end{center}
	\caption{An example table.}
	\label{table:example_table}
\end{table}
```

## Additional Info

For a more in depth article reviewing this library, see this [Medium post](https://towardsdatascience.com/how-to-create-latex-tables-directly-from-python-code-5228c5cea09a).  
A working example is also given in this [Colab Notebook](https://colab.research.google.com/drive/1Iq10lHznMngg1-Uoo-QtpTPii1JDYSQA?usp=sharing).  

## Release History

* 1.0.1
    * Fixed bug with multicolumn headers missing horizontal and vertical lines. Thanks to [electricbrass](https://github.com/electricbrass).   
* 1.0.0
    * Added the ability to a list of rows rather than a Texttable object (Texttable is still a requirement).
      Inspired by [latextable-lite](https://github.com/huisyy/latextable-lite) from [Huisyy](https://github.com/huisyy).
    * Added support for multi-column headers.
    * Added aliasing, where strings in the original data can be replaced before outputting to Latex (e.g., escaping characters).
    * Added docs via Read the Docs.
    * Updated build to pyproject.toml for PEP 621 compliance (thanks to [KOLANICH](https://github.com/KOLANICH)).
    * Fixed bug that occurs when texttable align is not set.
* 0.3.0
    * Added support for [short captions](https://tex.stackexchange.com/questions/11579/short-captions-for-figures-in-listoffigures)
      (thanks to [PhilW92](https://github.com/PhilW92)).
    * Added the ability to drop rows as well as columns.
    * Captions can now be placed above tables instead of below.
* 0.2.1
    * Removed row hlines when using booktabs.
* 0.2.0
    * Added support for booktabs and table positioning.
* 0.1.1
    * Minor changes to documentation.
* 0.1.0
    * Initial Release.

## Meta

Website: [Joseph Early](https://www.jearly.co.uk/)  
Twitter: [@JosephAEarly](https://twitter.com/JosephAEarly)  
Email: [joseph.early.ai@gmail.com](mailto:joseph.early.ai@gmail.com)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jearly)

Distributed under the MIT license. See [LICENSE](LICENSE) for more information.
