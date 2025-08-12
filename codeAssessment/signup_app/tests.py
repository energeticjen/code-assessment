from django.test import Client, TestCase

from .forms import UserForm
from .models import User

client = Client()

class UserModelTests(TestCase):

    def test__user_string_representation(self):
        user = User.objects.create(name="test", title="test_title")
        assert str(user) == "test"


class UserFormTests(TestCase):

    def test__user_form_requires_name(self):
        data = {"name": "", "title": "test_title"}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test__user_form_requires_title(self):
        data = {"name": "test", "title": ""}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())


class UserViewTests(TestCase):

    def test__view_homepage_response(self):
        response = client.get('/signup/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'signup/home.html')

    def test__data_saved(self):
        data = {"name": "test", "title": "test_title"}
        response = client.post('/signup/submit/', data=data, follow=True)
        self.assertTemplateUsed(response, "signup/confirm.html")
        user = User.objects.get(title="test_title")
        assert user.name == "test"

    def test__view_confirm(self):
        User.objects.create(name="test", title="test_title", age=20, hometown="test_town")
        response = client.get('/signup/confirm/')
        self.assertContains(response, '<td>test</td>')
