from unittest import TestCase, main

from progression import is_progression



class ProgressionTests(TestCase):

    def test_three_numbers(self):
        self.assertTrue(is_progression([1, 2, 3]))
        self.assertTrue(is_progression([1, 1, 1]))
        self.assertTrue(is_progression([1, 5, 9]))
        self.assertFalse(is_progression([1, 5, 10]))
        self.assertFalse(is_progression([1, 2, 5]))
        
    def test_to_little_numbers(self):
        self.assertFalse(is_progression([]))
        self.assertFalse(is_progression([1]))
        self.assertFalse(is_progression([1, 2]))

    def test_unorder_list(self):
        self.assertTrue(is_progression([3, 2, 1]))
        self.assertTrue(is_progression([2, 3, 1]))
        self.assertFalse(is_progression([10, 5, 1]))

    def test_long_list(self):
        self.assertTrue(is_progression([1, 2, 3, 4]))
        self.assertTrue(is_progression([1, 3, 5, 7, 9, 11, 13, 15]))
        self.assertFalse(is_progression([1, 2, 3, 4, 5, 6, 7, 8, 15]))

    def test_floats(self):
        self.assertTrue(is_progression([0.5, 1.0, 1.5, 2.0]))
        self.assertFalse(is_progression([0.5, 1.0, 1.5, 3.0]))



if __name__ == '__main__':
    main()        
