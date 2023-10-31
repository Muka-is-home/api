from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    if request.user.is_superuser:
        logout(request)
        return redirect('login')
    
    logout(request)
    return redirect('user_login')
