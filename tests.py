from django.test import SimpleTestCase


class TemplateTest(SimpleTestCase):
    def test_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Welcome to my website!')

