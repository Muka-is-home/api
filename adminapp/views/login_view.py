from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from adminapp.forms import CustomAuthenticationForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'adminapp/login/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        if self.request.user.is_active and self.request.user.is_staff:
            return reverse_lazy('index')
        elif self.request.user.is_active and not self.request.user.is_staff:
            return reverse_lazy('single_content', args=[1])
        return reverse_lazy('content')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password!')
        return self.render_to_response(self.get_context_data(form=form))
