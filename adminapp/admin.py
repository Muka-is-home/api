from django.contrib import admin
from django.template.response import TemplateResponse

from adminapp.views import UserAdminView
from api.models import User


class CustomAdminSite(admin.AdminSite):
    # The text to put at the end of each admin page’s <title> (a string). By default, this is “Django site admin”.
    site_title = "Django site admin"

    # Text to put in each page's <h1>.
    site_header = "Django administration"

    # Text to put at the top of the admin index page.
    index_title = "Site administration"

    # URL for the "View site" link at the top of each admin page.
    site_url = "/"

    # A boolean value that determines whether to show the navigation sidebar on larger screens
    enable_nav_sidebar = True

    # Subclass of AuthenticationForm that will be used by the admin site login view.
    login_form = None

    # Path to a custom template that will be used by the admin site main index view.
    index_template = "admin/index.html"

    # Path to a custom template that will be used by the admin site app index view.
    app_index_template = "admin/app_index.html"

    # Path to a custom template that will be used by the admin site login view.
    login_template = "admin/login.html"

    # Path to a custom template that will be used by the admin site logout view.
    logout_template = None

    # Path to a custom template that will be used by the admin site password change view.
    password_change_template = "admin/user/add_form.html"

    def get_urls(self):
        site_urls = []
        site_urls += UserAdminView(self.admin_view).urls()
        site_urls += super().get_urls()
        return site_urls


admin_site = CustomAdminSite(name="myadmin")

admin_site.register(User)
