from unittest import TestCase, main
from selenium import webdriver

class FizzBuzzAcceptanceTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_page_title(self):
        # Wojtek wants to play fizz buzz.
        # He goes to https:127.0.0:8000/ and sees a page titled FizzBuzz.
        self.assertIn("FizzBuzz", self.browser.title)

    def test_page_content(self):
        # The page gives short explanation "FizzBazz is ...".
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('FizzBuzz is', body.text)

    def assertInteraction(self, form_input, page_output):
        self.browser.remote('http://localhost:8000', {})
        #import ipdb
        #ipdb.set_trace()

        element = self.browser.find_element_by_name("fizzbuzz_number")
        element.send_keys(form_input)
        self.browser.find_element_by_id("Submit").click()
        self.browser.implicitly_wait(3)
        answer = self.browser.find_element_by_tag_name('h1')
        self.assertIn(page_output, answer.text)

    def test_interaction_with_page(self):
        # There is a also an input window and send batton.
        # After sending a 3, ther is a Fizz displayed on the page.
        self.assertInteraction('3', 'Fizz')
        # After sending a 5, ther is a Buzz diplayed.
        self.assertInteraction('5', 'Buzz')
        # And 15 gives back FizzBazz.
        self.assertInteraction('15', 'FizzBuzz')
        # 7 gives simply 7 as it cannot be devided neither by 3 nor by 5.
        self.assertInteraction('7', '7')
        
# When he tries to send a letter he sees a validation error.

if __name__ == '__main__':
    main()