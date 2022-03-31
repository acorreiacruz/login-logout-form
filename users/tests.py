from django.test import TestCase
from django.urls import reverse, resolve
from users.views import login

class UsersTest(TestCase):

    def test__users_login_url_is_correct(self):
        url = reverse('users:login')
        self.assertEqual("/users/",url)

    def test_login_view_functions_is_correct(self):
        resolve_object = resolve(reverse('users:login'))
        self.assertIs(login,resolve_object.func)

    def test_users_login_template_is_correct(self):
        ...