from adminapp.serializers import UserSerializer
from adminapp.views.utils import CustomAdminListView
from api.models import User


class UserAdminView(CustomAdminListView):

    def __init__(self, admin_view):
        CustomAdminListView.__init__(
            self,
            model=User, serializer=UserSerializer,
            base_path="users", admin_view=admin_view,
            title="User"
        )

    def urls(self):
        urls = []
        urls += CustomAdminListView.urls(self)

        print(urls, "**********")
        return urls
