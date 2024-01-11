from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_signup(request):
    return render(request, "adminapp/profile_signup.html")
