# texttable-latex

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  ![Build Status](https://github.com/JAEarly/texttable-latex/workflows/build/badge.svg)

[Texttable](https://github.com/foutaise/texttable) is a Python package that can create simple ASCII tables. This package extends its functionality to allow the table to be directly output in Latex, removing the tedious copy and paste chore. The Latex output matches the table design, and there are utilities for adding table captions and labels.

There is an [open pull request](https://github.com/foutaise/texttable/pull/68) to add these features directly to the Texttable library, but it has yet to get any attention so I've released it as its own library.

![](docs/cover_cropped.png)

## Features
- Draw a table object in a Latex format.
- Matches table decoration (border, header, hlines, vlines).
- Applies horizontal column alignment.
- Allows the user to drop certain columns from the output.
- Provides the ability to add a caption and reference label to the Latex output.
- The output is correctly indented for directly copying into Latex.

## Installation

[PyPi](https://pypi.org/project/texttable-latex/0.1.0/):

```
pip install texttable-latex
```

Requirements:

```
texttable
```

## Usage example

The single function `texttable.draw_latex(table)` returns a formatted Latex string based on the provided table.

### Examples
These examples use the existing tables provided in the Texttable docs.

Usage:

```
table = Texttable()
table.set_cols_align(["l", "r", "c"])
table.set_cols_valign(["t", "m", "b"])
table.add_rows([["Name", "Age", "Nickname"],
                ["Mr\nXavier\nHuon", 32, "Xav'"],
                ["Mr\nBaptiste\nClement", 1, "Baby"],
                ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"]])
print(table.draw() + "\n")
print(texttable_latex.draw_latex(table, caption="An example table.") + "\n")

table = Texttable()
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t',  # text
                      'f',  # float (decimal)
                      'e',  # float (exponent)
                      'i',  # integer
                      'a']) # automatic
table.set_cols_align(["l", "r", "r", "r", "l"])
table.add_rows([["text",    "float", "exp", "int", "auto"],
                ["abcd",    "67",    654,   89,    128.001],
                ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
print(table.draw() + "\n")
print(texttable_latex.draw_latex(table, caption="Another table.", label="table:another_table") + "\n")
print(texttable_latex.draw_latex(table, caption="A table with dropped columns.", label="table:dropped_column_table", drop_columns=['exp', 'int']))
```

Latex output:

```
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

\begin{table}
	\begin{center}
		\begin{tabular}{l r r r l}
			text & float & exp & int & auto \\
			\hline
			abcd & 67.000 & 6.540e+02 & 89 & 128.001 \\
			efghijk & 67.543 & 6.540e-01 & 90 & 1.280e+22 \\
			lmn & 0.000 & 5.000e-78 & 89 & 0.000 \\
			opqrstu & 0.023 & 5.000e+78 & 92 & 1.280e+22 \\
		\end{tabular}
	\end{center}
	\caption{Another table.}
	\label{table:another_table}
\end{table}

\begin{table}
	\begin{center}
		\begin{tabular}{l r r r l}
			text & float & auto \\
			\hline
			abcd & 67.000 & 128.001 \\
			efghijk & 67.543 & 1.280e+22 \\
			lmn & 0.000 & 0.000 \\
			opqrstu & 0.023 & 1.280e+22 \\
		\end{tabular}
	\end{center}
	\caption{A table with dropped columns.}
	\label{table:dropped_column_table}
\end{table}
```

## Release History

* 0.1.0
    * Initial Release

## Meta

[Joseph Early](https://www.jearly.co.uk/)  
[@JosephAEarly](https://twitter.com/dbader_org)  
joseph.early.ai@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.
