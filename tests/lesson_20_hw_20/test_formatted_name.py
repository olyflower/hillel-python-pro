import unittest

from lesson_20_hw_20.formatted_name import formatted_name


class TestFormattedName(unittest.TestCase):
    def test_full_name(self):
        self.assertEqual(formatted_name('Mary', 'Jons', middle_name='L'), 'Mary L Jons')

    def test_first_last_name(self):
        self.assertEqual(formatted_name('Mary', 'Jons'), 'Mary Jons')

    def test_lower_case(self):
        self.assertEqual(formatted_name('mary', 'jons', middle_name='l'), 'Mary L Jons')


if __name__ == '__main__':
    unittest.main()
