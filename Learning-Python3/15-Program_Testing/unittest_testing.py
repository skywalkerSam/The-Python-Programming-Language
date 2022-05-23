import unittest     # Testing Module
import script     # Python File to perform tests


class TestClass(unittest.TestCase):
    def setUp(self):
        ''' It'll run before running any function!'''
        print("A function is about to execute...")

    def test_do_stuff(self):
        """ Testing with unittest module """        # Docstrings, Remember?
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "hello"
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertFalse(result, "")

    def tearDown(self) -> None:
        print("Cleaning up everything for the next test to happen, Please Wait :)")
        return super().tearDown()


unittest.main()
