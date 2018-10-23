from django.test    import TestCase
from .forms         import UserRegistrationForm, ProfileRegistrationForm


class TestAccountsForms(TestCase):
    
    def test_registration_form(self):
        form=UserRegistrationForm({
            'username': 'test',
            'email':'test@gmail.com',
            'password1' : 'password1234_*/',
            'password2' : 'password1234_*/'
        })
        self.assertTrue(form.is_valid())
    
    # def test_profile_form(self):
    #     form=ProfileRegistrationForm({
    #         'user':'test',
    #         'adherent_number': '1234567',
    #         'rate_coefficient':'1',
    #     })
    #     self.assertTrue(form.is_valid())