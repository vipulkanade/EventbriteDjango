from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from .views import home, getEvents
from .forms import CategoriesForm
from .services import getCategoryID, results

import os

class SearchPageTest(TestCase):

    def test_home_page_url(self):
        pageFound = resolve('/')
        self.assertEqual(pageFound.func, home)

    def test_home_page_title_html(self):
        request = HttpRequest()
        response = home(request)

        self.assertIn(b'<title>Search Events</title>', response.content)
        self.assertTrue(response.content.endswith( b'</html>'))



class getEventPageTest(TestCase):

    def test_getEvents_page_url(self):
        pageFound = resolve('/results/')
        self.assertEqual(pageFound.func, getEvents)

    def test_getEvents_get_access(self):
        response = self.client.get('/results/', follow=True)
        self.assertRedirects(response, '/')

    def test_getEvents_post_access(self):
        testing_form_data = {
            'category_1': "music",
            'category_2': "business",
            'category_3': "food"
        }

        #testing a simple post without ajax
        response1 = self.client.post('/results/', testing_form_data) # blank data dictionary
        self.assertIn(b'<title>Search Results</title>', response1.content)
        self.assertTrue(response1.content.endswith(b'</html>'))

        #testing with ajax call
        response2 = self.client.post('/results/', {'page_id': 1}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertIn(b'<div class="thumbnail" >', response2.content)



class CategoriesFormTest(TestCase):

    def test_form(self):
        # Distinct categories. Assert True
        testing_form_data1 = {
            'category_1': "music",
            'category_2': "business",
            'category_3': "food"
        }

        #contains similar two categories. Assert False
        testing_form_data2 = {
            'category_1': "music",
            'category_2': "music",
            'category_3': "food"
        }

        #contains blank. Assert False
        testing_form_data3 = {
            'category_1': "",
            'category_2': "",
            'category_3': ""
        }

        form1 = CategoriesForm(data = testing_form_data1)
        form2 = CategoriesForm(data = testing_form_data2)
        form3 = CategoriesForm(data = testing_form_data3)

        self.assertTrue(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertFalse(form3.is_valid())



class EventbriteAPIRequestTest(TestCase):

    def test_eventbrite_api_request(self):
        testing_categories = ["music", "business", "food"]
        auth_token = os.environ.get('AUTH_TOKEN')
        testing_page_id = "1"
        response, status_code = results(testing_categories[0], testing_categories[1],
            testing_categories[2], testing_page_id, auth_token)

        self.assertEqual(status_code, 200)
        self.assertEqual("application/json", response.headers['content-type'])









