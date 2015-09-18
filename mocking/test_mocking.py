from unittest import main, TestCase
import mock

from sth import Sth


class Foo(TestCase):

    def test_foo(self):
        self.assertEqual(Sth().foo('a'), 'A')

    def test_bar(self):
        self.assertEqual(Sth().bar('a'), 'A')

    @mock.patch('sth.Sth.foo')
    def test_mock(self, mock_foo):
        mock_foo.return_value = 'foo bar'
        self.assertEqual(Sth().bar('s'), 'foo bar')
        self.assertTrue(mock_foo.called)

if __name__ == '__main__':
    main()
