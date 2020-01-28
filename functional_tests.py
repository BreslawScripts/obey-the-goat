from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He's invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "go checkout out 'Eloquent JavaScript'" into a text box (Simon's hobby is building websites)
        inputbox.send_keys('Buy Eloquent JavaScript')
        # Whe he hits enter, the page updates, and now the page lists:
        # 1: "Buy 'Eloquent JavaScript'" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy Eloquent JavaScript' for row in rows),
            "Ouch, man, here's your own failure message"
        )

        # There's still a text box inviting him to add another item. 
        # He enters "check for a review of online JavaScript learning resources" (Simon's very methodical)
        self.fail('Finish the test!')
        # The page updates again, and now shows both items on his list
        [...]
        # Simon wonders whether the site will remember his list. 
        # Then she sees that the site has generated a unique URL for him -- there is some explanatory text to that effect.

        # Simon visits that URL - his to-do list is still there.

        # Satisfied, he goes back to building his own website

if __name__ == '__main__':
    unittest.main(warnings='ignore')