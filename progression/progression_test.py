from unittest import TestCase, main

from progression import is_progression



class ProgressionTests(TestCase):

    def test_three_numbers(self):
        self.assertTrue(is_progression([1,2,3]))
        self.assertTrue(is_progression([1,1,1]))
        self.assertTrue(is_progression([1,5,9]))
        self.assertFalse(is_progression([1,5,10]))
        self.assertFalse(is_progression([1,2,5]))
        

if __name__ == '__main__':
    main()        
