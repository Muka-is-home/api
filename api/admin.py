from django.contrib import admin

# Register your models here.
from api.models import User, Tag, Content


class MyAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"


admin_site = MyAdminSite(name="myadmin")


admin_site.register(Tag)
admin_site.register(User)
admin_site.register(Content)
