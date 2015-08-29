from unittest import TestCase, main
from selenium import webdriver

class FizzBuzzAcceptanceTests(TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def test_page_title(self):
		# Wojtek wants to play fizz buzz.
		# He goes to https:127.0.0:8000/ and sees a page titled FizzBuzz.
		self.browser.get('http://localhost:8000')
		self.assertIn("FizzBuzz", self.browser.title)


# The page gives short explanation "FizzBazz is ...".
# There is a also an input window and send batton.
# After sending a 3, ther is a Fizz displayed on the page.
# After sending a 5, ther is a Buzz diplayed.
# And 15 gives back FizzBazz.
# When he tries to send a letter he sees a validation error.

if __name__ == '__main__':
	main()