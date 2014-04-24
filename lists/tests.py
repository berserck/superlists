from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePAgeViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = home_page(request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        print(response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))