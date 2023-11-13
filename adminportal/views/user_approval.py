from django.shortcuts import render
from django.core.mail import EmailMessage
from utils import get_env
from api.models import User
from adminportal.serializers.serializers import UserListSerializer

def update_approval(request):
    if request.method == "POST":
        users_to_approve = [value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken']
        env = get_env(__file__)
        for user in users_to_approve:
            status, user_id = user.split('--')
            user = User.objects.get(pk=user_id)
            if status == 'approved':
                user.active = True
                user.ready_for_approval = False
                user.save()
                email = EmailMessage(
                    'Welcome to Muka!',
                    'message body',
                    f'{env("EMAIL_HOST_USER")}',
                    [user.email]
                )
                email.send()
            elif status == 'rejected':
                user.active = False
                user.ready_for_approval = False
                user.save()
                email = EmailMessage(
                    'Concerning your profile at Muka',
                    'message body',
                    f'{env("EMAIL_HOST_USER")}',
                    [user.email]
                )
                email.send()
            elif status == 'ready':
                user.active = None
                user.ready_for_approval = True
                user.save()

        users = User.objects.exclude(user__is_superuser=True)
        
        user_data = UserListSerializer(users, many=True).data
        return render(request, "adminportal/user_list.html", {
            "users": user_data
        })
