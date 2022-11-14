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
       self.fail('write me!') 


# if __name__ == '__main__':  
#     unittest.main()
