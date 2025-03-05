import unittest


class MyTest01(unittest.TestCase):
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

    def test_01(self):
        for i in range(10):
            print("output: " + str(i))
        self.assertEqual(1, 1)

    def test_02(self):
        self.assertEqual(1, 2)
