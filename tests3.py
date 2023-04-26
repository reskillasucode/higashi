from django.test import SimpleTestCase
from myapp.forms import ContactForm

class FormTest(SimpleTestCase):
    def test_contact_form(self):
        form_data = {'name': 'Test User', 'email': 'testuser@example.com', 'message': 'This is a test message.'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
