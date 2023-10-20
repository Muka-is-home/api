from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'adminportal/login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('user_list')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password!')
        return self.render_to_response(self.get_context_data(form=form))
