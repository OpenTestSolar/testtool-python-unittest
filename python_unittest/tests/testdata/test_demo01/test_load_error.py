import unittest


class LoadErrorTest(unittest.TestCase):
    raise Exception("LoadErrorTest")

    def test_05(self):
        self.assertEqual(1, 1)

    def test_06(self):
        self.assertEqual(1, 2)
