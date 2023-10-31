from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User as AuthUser
from django.core.mail import EmailMessage
from utils import get_env
from api.models import User, UserType, Specialization, UserSpecialization, County, UserCounty, UserLicense, State
from adminapp.serializers import UserFormSerializer
from api.serializers import UserTypeSerializer, SpecializationSerializer, StateSerializer, CountySerializer

def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_data = UserFormSerializer(user).data
    if request.method == "POST":
        # process edit form
        user_type = UserType.objects.get(pk=request.POST.get("user_type"))

        user.name=request.POST.get("name")
        user.website=request.POST.get("website")
        user.bio=request.POST.get("bio")
        user.company=request.POST.get("company")
        user.company_address=request.POST.get("company_address")
        user.company_phone=request.POST.get("company_phone")
        user.contact_no=request.POST.get("contact_no")
        user.facebook=request.POST.get("facebook")
        user.user_type=user_type
        
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        tiktok = request.POST.get("tiktok")

        if facebook:
            user.facebook = facebook
        if instagram:
            user.instagram = instagram
        if tiktok:
            user.tiktok = tiktok
            
        user.save()

        for specialization in UserSpecialization.objects.filter(user=user):
            specialization.delete()

        for specialization in request.POST.getlist("specializations"):
            spec = Specialization.objects.get(pk=specialization)
            UserSpecialization.objects.create(
            user=user,
            specialization=spec
            )

        user_data = UserFormSerializer(user).data
        return render(request, "adminapp/user_detail.html", {
            "user": user_data
        })

    # render edit form
    user_types = UserType.objects.exclude(name="Admin")
    user_type_data = UserTypeSerializer(user_types, many=True).data

    specializations = Specialization.objects.all()
    specialization_data = SpecializationSerializer(specializations, many=True).data
    
    user_specialization_ids = user.specializations.values_list('specialization', flat=True)

    print(user_data["licenses"])
    return render(request, "adminapp/user_profile/edit_profile.html", {
    "user": user_data,
    "user_types": user_type_data,
    "specializations": specialization_data,
    "user_specializations": user_specialization_ids,
    })

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_data = UserFormSerializer(user).data
    return render(request, "adminapp/user_detail.html", {
        "user": user_data
    })

def create_profile(request, type):
    if request.method == "POST":
        if User.objects.filter(email=request.POST.get("email")):
            return render(request, "adminapp/email_taken.html", {
                "type": type
            })
        
        else:
            auth_user = AuthUser.objects.get(username=request.user)
            user_type = UserType.objects.get(name=type)
            user_profile = User(
                user=auth_user,
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                website=request.POST.get("website"),
                bio=request.POST.get("bio"),
                company=request.POST.get("company"),
                company_address=request.POST.get("company_address"),
                company_phone=request.POST.get("company_phone"),
                contact_no=request.POST.get("contact_no"),
                image=request.POST.get("image"),
                user_type=user_type
            )

            facebook = request.POST.get("facebook")
            instagram = request.POST.get("instagram")
            tiktok = request.POST.get("tiktok")

            if facebook:
                user_profile.facebook = facebook
            if instagram:
                user_profile.instagram = instagram
            if tiktok:
                user_profile.tiktok = tiktok

            user_profile.save()

            for specialization in request.POST.getlist("specializations"):
                spec = Specialization.objects.get(pk=specialization)
                UserSpecialization.objects.create(
                user=user_profile,
                specialization=spec
                )

            
            user_data = UserFormSerializer(user_profile).data
            if type == "Realtor":
                
                states = State.objects.all()
                state_data = StateSerializer(states, many=True).data

                counties = County.objects.all()
                county_data = CountySerializer(counties, many=True).data
                
                return render(request, "adminapp/user_profile_forms/user_licenses_form.html", {
                "states": state_data,
                "counties": county_data
                })
            else:
                user_profile.ready_for_approval = True
                user_profile.user.is_active = True
                user_profile.user.save()
                user_profile.save()
                return render(request, "adminapp/thank_you.html", {
                "user": user_data
                })

    specializations = Specialization.objects.all()
    specialization_data = SpecializationSerializer(specializations, many=True).data

    return render(request, "adminapp/user_profile_forms/profile_form.html", {
    "user": type,
    "specializations": specialization_data,
    })

def user_licenses(request):
    if request.method == 'POST':
        user_profile = User.objects.get(user=request.user)
        for county in request.POST.getlist("counties"):
            cty = County.objects.get(pk=county)
            UserCounty.objects.create(
                user=user_profile,
                county=cty
            )

        user_licenses = request.POST.get("userLicenses").split(",")
        for user_license in user_licenses:
            state_id, license_no = user_license.split("-")
            state = State.objects.get(pk=int(state_id))
            UserLicense.objects.create(
                state=state,
                user=user_profile,
                license_no = license_no
            )

        env = get_env(__file__)
        email_to_muka = EmailMessage(
                    f'new Muka applicant - {user_profile.name}',
                    f'{user_profile.name} has applied for a spot on Muka!',
                    f'{env("EMAIL_HOST_USER")}',
                    [env("EMAIL_HOST_USER")]
                )
        email_to_muka.send()
        email_to_user = EmailMessage(
                    f'Thanks for your application {user_profile.name}!',
                    f'{user_profile.name}, We will review your profile and submit or reject you.',
                    f'{env("EMAIL_HOST_USER")}',
                    [user_profile.email]
                )
        email_to_muka.send()
        email_to_user.send()

        user_profile.ready_for_approval = True
        user_profile.save()
        user_profile.user.is_active = True
        user_profile.user.save()
        user_data = UserFormSerializer(user_profile).data
        return render(request, "adminapp/thank_you.html", {
            "user": user_data
        })
