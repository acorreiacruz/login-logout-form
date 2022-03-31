from django.test import TestCase
from django.urls import reverse

class UsersTest(TestCase):

    def test_login_view_url_is_correct(self):
        url = reverse('users:login')
        self.assertEqual("/users/",url)