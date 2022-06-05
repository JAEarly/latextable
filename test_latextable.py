import unittest

import latextable


class LatexTableTest(unittest.TestCase):

    def test_clean_row(self):
        row = ["Row1\n", "Row2"]
        cleaned = latextable._clean_row(row)
        self.assertEqual(cleaned[0], "Row1")
        self.assertNotIn("\n", cleaned[0])
        self.assertEqual(cleaned[1], "Row2")

    def test_sanitise_drop_columns(self):
        header = ["Col1", "Col2", "Col3"]
        self.assertIsNone(latextable._sanitise_drop_columns(header, ["Col1"]))
        self.assertIsNone(latextable._sanitise_drop_columns(header, ["Col1", "Col2"]))
        self.assertRaises(latextable.DropColumnError, latextable._sanitise_drop_columns, header, ["Col4"])

    def test_drop_columns(self):
        target = ["Row1", "Row2", "Row3"]
        header = ["Col1", "Col2", "Col3"]
        no_drop = latextable._drop_columns(target, header, [])
        one_drop = latextable._drop_columns(target, header, ['Col1'])
        two_drop = latextable._drop_columns(target, header, ['Col1', 'Col3'])
        self.assertEqual(len(no_drop), 3)
        self.assertTrue(target[0] in no_drop)
        self.assertTrue(target[1] in no_drop)
        self.assertTrue(target[2] in no_drop)
        self.assertEqual(len(one_drop), 2)
        self.assertTrue(target[0] not in one_drop)
        self.assertTrue(target[1] in one_drop)
        self.assertTrue(target[2] in one_drop)
        self.assertEqual(len(two_drop), 1)
        self.assertTrue(target[0] not in two_drop)
        self.assertTrue(target[1] in two_drop)
        self.assertTrue(target[2] not in two_drop)

    def test_sanitise_drop_rows(self):
        rows = [["R0C0", "R0C1", "R0C2"],
                ["R1C0", "R1C1", "R1C2"],
                ["R2C0", "R2C1", "R2C2"]]
        self.assertIsNone(latextable._sanitise_drop_rows(len(rows), [2]))
        self.assertIsNone(latextable._sanitise_drop_rows(len(rows), [0, 2]))
        self.assertRaises(latextable.DropRowError, latextable._sanitise_drop_rows, len(rows), [-1])
        self.assertRaises(latextable.DropRowError, latextable._sanitise_drop_rows, len(rows), [3])
        self.assertRaises(latextable.DropRowError, latextable._sanitise_drop_rows, len(rows), [-1, 3])

    def test_drop_rows(self):
        rows = [["R0C0", "R0C1", "R0C2"],
                ["R1C0", "R1C1", "R1C2"],
                ["R2C0", "R2C1", "R2C2"]]
        no_drop = latextable._drop_rows(rows, [])
        one_drop = latextable._drop_rows(rows, [2])
        two_drop = latextable._drop_rows(rows, [0, 1])
        self.assertEqual(len(no_drop), 3)
        self.assertTrue(["R0C0", "R0C1", "R0C2"] in no_drop)
        self.assertTrue(["R1C0", "R1C1", "R1C2"] in no_drop)
        self.assertTrue(["R2C0", "R2C1", "R2C2"] in no_drop)
        self.assertEqual(len(one_drop), 2)
        self.assertTrue(["R0C0", "R0C1", "R0C2"] in one_drop)
        self.assertTrue(["R1C0", "R1C1", "R1C2"] in one_drop)
        self.assertTrue(["R2C0", "R2C1", "R2C2"] not in one_drop)
        self.assertEqual(len(two_drop), 1)
        self.assertTrue(["R0C0", "R0C1", "R0C2"] not in two_drop)
        self.assertTrue(["R1C0", "R1C1", "R1C2"] not in two_drop)
        self.assertTrue(["R2C0", "R2C1", "R2C2"] in two_drop)

    def test_indent_text(self):
        text = "test"
        no_ident = latextable._indent_text(text, 0)
        one_ident = latextable._indent_text(text, 1)
        two_ident = latextable._indent_text(text, 2)
        self.assertIn(text, no_ident)
        self.assertEqual(len(no_ident), len(text))
        self.assertIn(text, one_ident)
        self.assertEqual(len(one_ident) - 1, len(text))
        self.assertIn(text, two_ident)
        self.assertEqual(len(two_ident) - 2, len(text))


if __name__ == '__main__':
    unittest.main()
