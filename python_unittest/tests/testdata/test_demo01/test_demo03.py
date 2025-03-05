import unittest


class MyTest03(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("UnitTest Begin...")

    @classmethod
    def tearDownClass(self):
        print("UnitTest End...")

    def setUp(self):
        print("Begin...")

    def tearDown(self):
        print("End...")

    def test_05(self):
        self.assertEqual(1, 1)

    def test_06(self):
        self.assertEqual(1, 2)
