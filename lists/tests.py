from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class SmokeTest(TestCase): 
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # checking that resolve() finds a function called home_page 
        self.assertEqual(found.func, home_page)