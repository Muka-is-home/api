from django.shortcuts import render, get_object_or_404
from api.models import User
from adminapp.serializers import UserFormSerializer

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_data = UserFormSerializer(user).data
    return render(request, "adminapp/user_detail.html", {
        "user": user_data
    })
