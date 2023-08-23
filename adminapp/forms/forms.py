from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from api.models import User

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class CustomPasswordResetForm(PasswordResetForm):
    def get_users(self, email=None):
        if email is None:
            email = self.cleaned_data.get('email')
        return User.objects.filter(email=email)
