from texttable import Texttable
import latextable


def run():
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()
    example_10()
    example_11()
    example_12()
    example_13()


def example_1():
    # Example 1 - Basic
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


def example_2():
    # Example 2 - Drop columns
    table_2 = Texttable()
    table_2.set_deco(Texttable.HEADER)
    table_2.set_cols_dtype(['t', 'f', 'e', 'i', 'a'])
    table_2.set_cols_align(["l", "r", "r", "r", "l"])
    table_2.add_rows([["text",    "float", "exp", "int", "auto"],
                     ["abcd",    "67",    654,   89,    128.001],
                     ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                     ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                     ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
    print('\n-- Example 2: Drop Columns --')
    print('Texttable Output:')
    print(table_2.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_2, caption="A table with dropped columns.", label="table:dropped_column_table",
                                drop_columns=['exp', 'int']))


def example_3():
    # Example 3 - Position
    table_3 = Texttable()
    table_3.set_cols_align(["c"] * 4)
    table_3.set_deco(Texttable.HEADER | Texttable.VLINES)
    table_3.add_rows([['Rocket', 'Organisation', 'LEO Payload (Tonnes)', 'Maiden Flight'],
                     ['Saturn V', 'NASA', '140', '1967'],
                     ['Space Shuttle', 'NASA', '24.4', '1981'],
                     ['Falcon 9 FT-Expended', 'SpaceX', '22.8', '2017'],
                     ['Ariane 5 ECA', 'ESA', '21', '2002']])
    print('\n-- Example 3: Position --')
    print('Texttable Output:')
    print(table_3.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_3, caption="A table with position.", label="table:position", position='ht'))


def example_4():
    # Example 4 - Booktabs
    table_4 = Texttable()
    table_4.set_cols_align(["c"] * 4)
    table_4.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.BORDER | Texttable.HLINES)
    table_4.add_rows([['Rank', 'Driver', 'Country', 'Wins'],
                      ['1', 'Lewis Hamilton', 'United Kingdom', '99'],
                      ['2', 'Michael Schumacher', 'Germany', '91'],
                      ['3', 'Sebastian Vettel', 'Germany', '53']])
    print('\n-- Example 4: Booktabs --')
    print('Texttable Output:')
    print(table_4.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_4, caption="A table using booktabs.", label="table:booktabs", use_booktabs=True))


def example_5():
    # Example 5 - Short Caption
    table_5 = Texttable()
    table_5.set_cols_align(["c"] * 3)
    table_5.set_deco(Texttable.HEADER | Texttable.BORDER)
    table_5.add_rows([['Company', 'Market Cap', 'Country'],
                      ['Apple', '2.425T', 'USA'],
                      ['Saudi Aramco', '2.358T', 'Saudi Arabia'],
                      ['Microsoft', '2.011T', 'USA']])
    print('\n-- Example 5: Short Caption --')
    print('Texttable Output:')
    print(table_5.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_5, caption="A table with a short caption.", label="table:short_caption",
                                caption_short="Short caption"))


def example_6():
    # Example 6 - Drop rows
    table_6 = Texttable()
    table_6.set_deco(Texttable.HEADER)
    table_6.set_cols_align(["c"] * 3)
    table_6.add_rows([['Position', 'Team', 'Points'],
                      ['1', 'Fulham', '90'],
                      ['2', 'Bournemouth', '88'],
                      ['3', 'Huddersfield', '82'],
                      ['4', 'Nottingham Forest', '80']])
    print('\n-- Example 6: Drop Rows --')
    print('Texttable Output:')
    print(table_6.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_6, caption="A table with dropped rows.", label="table:dropped_rows",
                                drop_rows=[1, 2]))


def example_7():
    # Example 7 - Caption above
    table_7 = Texttable()
    table_7.set_deco(Texttable.HEADER | Texttable.VLINES)
    table_7.set_cols_align(["c"] * 3)
    table_7.add_rows([['Rank', 'Name', 'ELO'],
                      ['1', 'Stockfish 15', '3541'],
                      ['2', 'Dragon by Komodo', '3535'],
                      ['3', 'Fat Fritz', '3518']])
    print('\n-- Example 7: Caption Above --')
    print('Texttable Output:')
    print(table_7.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_7, caption="This caption is above the table!", label="table:caption_above",
                                caption_above=True))


def example_8():
    # Example 8 - Test with no align
    table_8 = Texttable()
    table_8.add_rows([["A", "B", "C"],
                     ["a1", "b1", "c1"],
                     ["a2", "b2", "c2"],
                     ["a3", "b3", "c3"]])
    print('\n-- Example 8: Without texttable align --')
    print('Texttable Output:')
    print(table_8.draw())
    print('\nLatextable Output:')
    print(latextable.draw_latex(table_8, use_booktabs=True))


def example_9():
    # Example 9 - Test without using texttable
    rows = [["A", "B", "C"],
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a3", "b3", "c3"]]
    print('\n-- Example 9: Without using texttable table --')
    print('Latextable Output:')
    print(latextable.draw_latex(rows, use_booktabs=True))


def example_10():
    # Example 10 - Multicolumn header
    rows = [["R", "A", "B", "C", "D"],
            ["1", "a1", "b1", "c1", "d1"],
            ["2", "a2", "b2", "c2", "d2"],
            ["3", "a3", "b3", "c3", "d3"]]
    multicolumn_header = [("", 1), ("AB", 2), ("CD", 2)]
    print('\n-- Example 10: Multicolumn header --')
    print('Latextable Output:')
    print(latextable.draw_latex(rows, use_booktabs=True, multicolumn_header=multicolumn_header))


def example_11():
    # Example 11 - Multicolumn header with drop column
    rows = [["R", "A", "B", "C", "D"],
            ["1", "a1", "b1", "c1", "d1"],
            ["2", "a2", "b2", "c2", "d2"],
            ["3", "a3", "b3", "c3", "d3"]]
    multicolumn_header = [("", 1), ("AB", 2), ("", 1)]
    print('\n-- Example 11: Multicolumn header with drop column --')
    print('Latextable Output:')
    print(latextable.draw_latex(rows, use_booktabs=True, drop_columns=['C'], multicolumn_header=multicolumn_header))


def example_12():
    # Example 12 - Alias '&' in header and '+-' in rows
    rows = [["A", "B", "C & D"],
            ["a1", "b1", "c1 +- d1"],
            ["a2", "b2", "c2 +- d2"],
            ["a3", "b3", "c3 +- d3"]]
    alias = {'&': '\\&', '+-': '$\\pm$'}
    print('\n-- Example 12: Alias Test --')
    print('Latextable Output:')
    print(latextable.draw_latex(rows, use_booktabs=True, alias=alias))


def example_13():
    # Example 13 - Multicolumn header with vertical and horizontal lines
    rows = [["R", "A", "B", "C", "D"],
            ["1", "a1", "b1", "c1", "d1"],
            ["2", "a2", "b2", "c2", "d2"],
            ["3", "a3", "b3", "c3", "d3"]]
    multicolumn_header = [("", 1), ("AB", 2), ("CD", 2)]

    table_13 = Texttable()
    table_13.add_rows(rows)
    print('\n-- Example 13: Multicolumn header with vertical and horizontal lines --')
    print('Texttable Output:')
    print(table_13.draw())
    print('Latextable Output:')
    print(latextable.draw_latex(table_13, multicolumn_header=multicolumn_header))


if __name__ == "__main__":
    run()
