from django.shortcuts import render
from django.urls import path


class CustomAdminListView():

    def __init__(self, model, serializer, base_path, admin_view, title):
        self.base_path = base_path
        self.admin_view = admin_view
        self.model = model
        self.serializer = serializer
        self.title = title

    def urls(self):
        urls = [
            path(
                f"{self.base_path}/",
                self.admin_view(self.list),
                name=f"{self.base_path}-list"
            )
        ]
        return urls

    def list(self, request):
        query_set = self.model.objects.all()
        data = self.serializer(query_set, many=True).data
        return render(request, "admin/list.html", {
            "data": data,
            "headers": self.serializer._meta.get,
            "name": self.title,
            "header_text": f"All {self.title}s",
            "links": False
        })
