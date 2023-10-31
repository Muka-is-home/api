from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from adminapp.forms import CustomAuthenticationForm
from api.models import User

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'adminapp/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        try:
          user = User.objects.get(user=self.request.user)
          if user.active:
            return reverse_lazy('user_detail', args=[user.id])
          elif user.active is None:
            return reverse_lazy('thank_you')
          else:
            return reverse_lazy('rejection')
            
        except User.DoesNotExist:
          return reverse_lazy('profile_signup')

    def form_invalid(self, form):
        print(self.request)
        messages.error(self.request,'Invalid username or password!')
        return self.render_to_response(self.get_context_data(form=form))
