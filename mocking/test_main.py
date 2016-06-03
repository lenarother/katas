# mocking input function in tests for python3

from unittest import TestCase, main
from unittest.mock import patch

from main import read_input


class TestMockInput(TestCase):

    @patch('builtins.input', lambda x:'Kristian')
    def test_main(self):
        self.assertEqual(read_input(), 'Kristian')


if __name__ == '__main__':
    main()
