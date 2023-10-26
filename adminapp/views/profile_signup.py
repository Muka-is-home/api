from django.shortcuts import render

def profile_signup(request):
    return render(request, "adminapp/profile_signup.html")
