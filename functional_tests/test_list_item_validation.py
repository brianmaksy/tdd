import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import WebDriverException
from .base import FunctionalTest

import unittest

from lists.models import Item

MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(  
        self.browser.find_element_by_css_selector('.has-error').text,
        "You can't have an empty list item"
        ))

        # She tries again with some text for the item, which now works
        self.fail('finish this test!')


# if __name__ == '__main__':  
#     unittest.main()
