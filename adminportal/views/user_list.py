from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from api.models import User
from adminportal.serializers.serializers import UserListSerializer

def user_is_superuser(user):
    return user.is_superuser

@user_passes_test(user_is_superuser, login_url="user_login")
def user_list(request):
    # order by descending id so newest additions will show first
    user_list = User.objects.exclude(user__is_superuser=True).order_by('-id')
    
    paginator = Paginator(user_list, 10)
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    return render(request, "adminportal/user_list.html", {
        "users": users
    })
