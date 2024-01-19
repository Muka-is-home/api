from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from adminportal.views import user_is_superuser
from api.models import User

@user_passes_test(user_is_superuser, login_url='user_login')
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.user.delete()
    return redirect('user_list')
