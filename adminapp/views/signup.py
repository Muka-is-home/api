from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user without committing to the database
            user = form.save(commit=False)
            # Set the user's 'is_active' attribute to False
            user.is_active = False
            
            # Save the user to the database
            user.save()

            # Authenticate the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('profile_signup')
    else:
        form = UserCreationForm()
    return render(request, 'adminapp/signup.html', {'form': form})
