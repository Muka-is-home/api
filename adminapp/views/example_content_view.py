from django.shortcuts import render, get_object_or_404
from api.models import Content, User, ContentType
from api.serializers import ContentSerializer, UserSerializer, ContentTypeSerializer

def content_view(request, content_id=None, is_edit=None):
    request_method = request.method

    if is_edit:
        # Not finished, Use as an example
        content = get_object_or_404(Content, pk=content_id)
        content_data = ContentSerializer(content).data

        authors = User.objects.all()
        author_data = UserSerializer(authors, many=True).data

        content_types = ContentType.objects.all()
        content_types_data = ContentTypeSerializer(
            content_types, many=True).data

        return render(request, "adminapp/content_example/edit.html", {"content": content_data, "authors": author_data, "content_types": content_types_data})

    if request_method == "GET":
        if content_id:
            content = get_object_or_404(Content, pk=content_id)
            content_data = ContentSerializer(content).data
            return render(request, "adminapp/content_example/details.html", {"content": content_data})
        else:
            content = Content.objects.all()
            content_data = ContentSerializer(content, many=True).data
            return render(request, "adminapp/content_example/list.html", {"all_content": content_data})

    elif request_method == "POST":
        form_data = request.POST
        print(form_data["actual_method"])

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            content = get_object_or_404(Content, pk=content_id)
            content_data = ContentSerializer(content).data
            return render(request, "adminapp/content_example/edit.html", {"content": content_data})
        elif ("actual_method" in form_data
              and form_data["actual_method"] == "DELETE"):
            content = get_object_or_404(Content, pk=content_id)
            content_data = ContentSerializer(content).data
            return render(request, "adminapp/content_example/details.html", {"content": content_data})

    return render(request, "adminapp/index.html", {})
