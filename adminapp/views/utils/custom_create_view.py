from django.shortcuts import render
from django.urls import path


class CustomAdminCreateView():

    def __init__(self, model, serializer, base_path, admin_view, title):
        self.base_path = base_path
        self.admin_view = admin_view
        self.model = model
        self.serializer = serializer
        self.title = title

    def urls(self):
        urls = [
            path(
                f"{self.base_path}/create",
                self.admin_view(self.create),
                name=f"{self.base_path}-list"
            )
        ]
        return urls

    def create(self, request):
        query_set = self.model.objects.all()
        data = self.serializer(query_set, many=True).data
        return render(request, "admin/list.html", {
            "data": data,
            "headers": [self.serializer.Meta.fields],
            "name": self.title,
            "header_text": f"All {self.title}s",
            "links": False
        })
