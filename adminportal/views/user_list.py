from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from api.models import User
from adminportal.serializers.serializers import UserListSerializer

def user_is_superuser(user):
    return user.is_superuser

@user_passes_test(user_is_superuser)
def user_list(request):
    users = User.objects.exclude(user__is_superuser=True)
    user_data = UserListSerializer(users, many=True).data
    return render(request, "adminportal/user_list.html", {
        "users": user_data
    })
