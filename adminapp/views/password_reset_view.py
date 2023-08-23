from django.contrib.auth.views import PasswordResetView
from adminapp.forms import CustomPasswordResetForm

class PasswordReset(PasswordResetView):
    form_class=CustomPasswordResetForm
    