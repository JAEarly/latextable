from texttable import Texttable
import latextable


def run():
    example_1()
    example_2()
    example_3()
    example_4()


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


if __name__ == "__main__":
    run()
