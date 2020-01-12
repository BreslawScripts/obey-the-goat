from selenium import webdriver
import unittest

class NewVisitorTest (unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Simon's heard about a cool new online to-do app. He checks out its homepage
        self.browser.get('http://localhost:8000')

        # He notices that the page title and header mention "to-do lists"
        self.assertIn ('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He's invited to enter a to-do item straight away

        # He types "go checkout out 'Eloquent JavaScript'" into a text box (Simon's hobby is building websites)

        # Whe he hits enter, the page updates, and now the page lists:
        # 1: "Buy 'Eloquent JavaScript'" as an item in a to-do list

        # There's still a text box inviting him to add another item. 
        # He enters "check for a review of online JavaScript learning resources" (Simon's very methodical)

        # The page updates again, and now shows both items on his list

        # Simon wonders whether the site will remember his list. 
        # Then she sees that the site has generated a unique URL for him -- there is some explanatory text to that effect.

        # Simon visits that URL - his to-do list is still there.

        # Satisfied, he goes back to building his own website

if __name__ == '__main__':
    unittest.main(warnings='ignore')