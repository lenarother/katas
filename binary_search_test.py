from unittest import TestCase, main
from binary_search import recoursive_chop

class BinarySortTests(TestCase):

    def test_recoursive_chop(self):
        self.assertEqual(-1, recoursive_chop(3, []))
        self.assertEqual(-1, recoursive_chop(3, [1]))
        self.assertEqual(0,  recoursive_chop(1, [1]))
        #
        self.assertEqual(0,  recoursive_chop(1, [1, 3, 5]))
        self.assertEqual(1,  recoursive_chop(3, [1, 3, 5]))
        self.assertEqual(2,  recoursive_chop(5, [1, 3, 5]))
        self.assertEqual(-1, recoursive_chop(0, [1, 3, 5]))
        self.assertEqual(-1, recoursive_chop(2, [1, 3, 5]))
        self.assertEqual(-1, recoursive_chop(4, [1, 3, 5]))
        self.assertEqual(-1, recoursive_chop(6, [1, 3, 5]))
        #
        self.assertEqual(0,  recoursive_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1,  recoursive_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2,  recoursive_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3,  recoursive_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, recoursive_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, recoursive_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, recoursive_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, recoursive_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, recoursive_chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    main()