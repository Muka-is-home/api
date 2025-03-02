from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User as AuthUser
from django.core.mail import EmailMessage
from utils import get_env, handle_image_upload, signup_email_body
from api.models import User, UserType, Specialization, UserSpecialization, County, UserCounty, UserLicense, State
from adminapp.serializers import UserFormSerializer
from api.serializers import SpecializationSerializer, StateSerializer, CountySerializer
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request, pk, type):
    user = get_object_or_404(User, pk=pk)
    user_data = UserFormSerializer(user).data
    if request.method == "POST":
        # process edit form
        email_user = User.objects.filter(email=request.POST.get("email")).first()
        if email_user and email_user != user:
            return render(request, "adminapp/email_taken.html", {
                "type": type,
                "edit": True,
                "pk": pk
            })
        
        else:
            name = request.POST.get("name")
            image = handle_image_upload(request, name)
            
            if image is not None:
                user.image = image
            
            email = request.POST.get("email")
            user.user.email = email
            user.user.save()
            
            user.name=name
            user.website=request.POST.get("website")
            user.email=email
            user.bio=request.POST.get("bio")
            user.company=request.POST.get("company")
            user.company_address=request.POST.get("company_address")
            user.company_phone=request.POST.get("company_phone")
            user.contact_no=request.POST.get("contact_no")
            user.facebook=request.POST.get("facebook")
            
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

    specializations = Specialization.objects.all()
    specialization_data = SpecializationSerializer(specializations, many=True).data
    
    user_specialization_ids = user.specializations.values_list('specialization', flat=True)

    return render(request, "adminapp/user_profile_forms/edit_profile_form.html", {
    "user": user_data,
    "type": type,
    "specializations": specialization_data,
    "user_specializations": user_specialization_ids,
    })

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_data = UserFormSerializer(user).data
    if request.user.is_superuser or request.user == user.user:
        return render(request, "adminapp/user_detail.html", {
            "user": user_data
        })
    else:
        return render(request, "adminportal/access_denied.html")
    
@login_required
def create_profile(request, type):
    
    if request.method == "POST":
        email = request.POST.get("email")
        
        if User.objects.filter(email=email):
            return render(request, "adminapp/email_taken.html", {
                "type": type
            })
        
        else:
            
            request.user.email = email
            request.user.save()
            user_type = UserType.objects.get(name=type)
            
            name = request.POST.get("name")
            image = handle_image_upload(request, name)
            user_profile = User(
                user=request.user,
                name=name,
                email=email,
                website=request.POST.get("website"),
                bio=request.POST.get("bio"),
                company=request.POST.get("company"),
                company_address=request.POST.get("company_address"),
                company_phone=request.POST.get("company_phone"),
                contact_no=request.POST.get("contact_no"),
                image=image,
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

            states = State.objects.all()
            state_data = StateSerializer(states, many=True).data

            counties = County.objects.all()
            county_data = CountySerializer(counties, many=True).data
                
            return render(request, "adminapp/user_profile_forms/user_licenses_form.html", {
            "states": state_data,
            "counties": county_data
            })
                
    specializations = Specialization.objects.all()
    specialization_data = SpecializationSerializer(specializations, many=True).data

    return render(request, "adminapp/user_profile_forms/profile_form.html", {
    "user": type,
    "specializations": specialization_data
    })

@login_required
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
        if len(user_licenses[0]):
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
                    f'Review New User Signup! {user_profile.name}',
                    f'{user_profile.name} has signed up. Login to https://web.mukaishome.com/muka/login to approve or reject.',
                    f'Muka <{env("EMAIL_HOST_USER")}>',
                    ['hello@mukaishome.com','muka.web.dev@gmail.com']
                )
        email_to_muka.send()

        email_to_user = EmailMessage(
                    f'Thank You for Taking the First Step!',
                    signup_email_body(user_profile.name),
                    f'Muka <{env("EMAIL_HOST_USER")}>',
                    [user_profile.email]
                )
        email_to_user.send()

        user_profile.ready_for_approval = True
        user_profile.save()
        user_profile.user.is_active = True
        user_profile.user.save()
        user_data = UserFormSerializer(user_profile).data
        return render(request, "adminapp/thank_you.html")

@login_required
def edit_licenses(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        
        for county in UserCounty.objects.filter(user=user):
            county.delete()
        
        for user_license in UserLicense.objects.filter(user=user):
            user_license.delete()
            
        for county in request.POST.getlist("counties"):
            cty = County.objects.get(pk=county)
            UserCounty.objects.create(
                user=user,
                county=cty
            )
            
        user_licenses = request.POST.get("userLicenses").split(",")
        if len(user_licenses[0]):
            for user_license in user_licenses:
                state_id, license_no = user_license.split("-")
                state = State.objects.get(pk=int(state_id))
                UserLicense.objects.create(
                    state=state,
                    user=user,
                    license_no=license_no
                )
        user_data = UserFormSerializer(user).data
        return render(request, "adminapp/user_detail.html", {
            "user": user_data
        })
    
    states = State.objects.all()
    state_data = StateSerializer(states, many=True).data

    counties = County.objects.all()
    county_data = CountySerializer(counties, many=True).data
    
    user_county_ids = user.counties.values_list('county', flat=True)
    
    user_data = UserFormSerializer(user).data
    return render(request, "adminapp/user_profile_forms/edit_licenses_form.html", {
        "user": user_data,
        "states": state_data,
        "counties": county_data,
        "user_counties": user_county_ids,
        "licenses": user_data["licenses"]
    })

@login_required
def update_profile_picture(request, pk):
    
    image = handle_image_upload(request, request.POST.get("slug"))
    
    if image:
        
        user = User.objects.get(pk=pk)
        user.image = image
        user.save()
        
        user_data = UserFormSerializer(user).data
        return render(request, "adminapp/user_detail.html", {
            "user": user_data
        })

    return redirect("user_list")
