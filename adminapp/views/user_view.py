from django.shortcuts import render, get_object_or_404
from api.models import User, UserType, Specialization, UserSpecialization
from adminapp.serializers import UserFormSerializer
from api.serializers import UserTypeSerializer, SpecializationSerializer

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

        for specialization in UserSpecialization.objects.filter(user=user):
            specialization.delete()

        for specialization in request.POST.getlist("specializations"):
            spec = Specialization.objects.get(pk=specialization)
            UserSpecialization.objects.create(
            user=user,
            specialization=spec
            )

        user.save()
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
    return render(request, "adminapp/user_profile/user_detail.html", {
        "user": user_data
    })

def create_profile(request, type):
    if request.method == "POST":
            # process rest of profile form
            user_type = UserType.objects.get(pk=request.POST.get("user_type"))
            user_profile = User(
                user=request.user,
                name=request.POST.get("name"),
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
            return render(request, "adminapp/user_profile/user_detail.html", {
        "user": user_data
    })
    
    user_types = UserType.objects.exclude(name="Admin")
    user_type_data = UserTypeSerializer(user_types, many=True).data

    specializations = Specialization.objects.all()
    specialization_data = SpecializationSerializer(specializations, many=True).data

    return render(request, "adminapp/user_profile_forms/profile_form.html", {
    "user": type,
    "user_types": user_type_data,
    "specializations": specialization_data,
    })
