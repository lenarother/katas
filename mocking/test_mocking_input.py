# mocking input function in tests for python3

from unittest import TestCase, main
from unittest.mock import patch


def read_input():
    sth = input("Write something: ")
    return sth


TEST_DATA = iter(['Ewa', 'Wojtek', 'Lena', 'Kristian'])


class TestMockInput(TestCase):

    @patch('builtins.input', lambda x: 'Kristian')
    def test_main(self):
        self.assertEqual(read_input(), 'Kristian')

    @patch('builtins.input', lambda x: next(TEST_DATA))
    def test_main_with_iter(self):
        self.assertEqual(read_input(), 'Ewa')
        self.assertEqual(read_input(), 'Wojtek')
        self.assertEqual(read_input(), 'Lena')
        self.assertEqual(read_input(), 'Kristian')






if __name__ == '__main__':
    main()
