import unittest


class MyTest02(unittest.TestCase):
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

    def test_03(self):
        self.assertEqual(1, 1)

    def test_04(self):
        self.assertEqual(1, 2)
