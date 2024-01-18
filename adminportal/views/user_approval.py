from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test
from utils import get_env, rejection_email_body, approval_email_body
from api.models import User
from adminportal.serializers.serializers import UserListSerializer
from adminportal.views import user_is_superuser

@user_passes_test(user_is_superuser, login_url="user_login")
def update_approval(request):
    if request.method == "POST":
        users_to_approve = [value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken']
        env = get_env(__file__)
        for user in users_to_approve:
            status, user_id = user.split('--')
            user = User.objects.get(pk=user_id)
            if status == 'approved':
                if not user.active:
                    user.active = True
                    user.ready_for_approval = False
                    user.save()
                    email = EmailMessage(
                        'WELCOME HOME!',
                        approval_email_body(user.name),
                        f'{env("EMAIL_HOST_USER")}',
                        [user.email]
                    )
                    email.send()
            elif status == 'rejected':
                if user.active is None or user.active == True:
                    user.active = False
                    user.ready_for_approval = False
                    user.save()
                    email = EmailMessage(
                        'Your Application Status with Muka',
                        rejection_email_body(user.name),
                        f'{env("EMAIL_HOST_USER")}',
                        [user.email]
                    )
                    email.send()
            elif status == 'ready':
                user.active = None
                user.ready_for_approval = True
                user.save()
            
            elif status == 'inactive':
                user.active = False
                user.ready_for_approval = True
                user.save()

        users = User.objects.exclude(user__is_superuser=True)
        
        user_data = UserListSerializer(users, many=True).data
        return render(request, "adminportal/user_list.html", {
            "users": user_data,
            "submit_alert": True
        })
