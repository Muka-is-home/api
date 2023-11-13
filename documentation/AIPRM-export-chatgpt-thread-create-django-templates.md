
Exported with AIPRM <https://www.aiprm.com> by Trinity Christiana Terry (Trinity Christiana) on 8/9/2023, 8:20:09 PM

---

**User:**
Give me the steps to create a view in Django using templates without using Model Forms. I want full crud.

---

**ChatGPT:**
Sure! Creating a full CRUD (Create, Read, Update, Delete) in Django using templates without Model Forms involves the following steps:

1. <strong>Models</strong>: First, define your model in <code>models.py</code>.

    ```python
    # models.py
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    ```

1. <strong>URLs</strong>: Define URLs for your CRUD operations in <code>urls.py</code>.

    ```python
    # urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('items/', views.item_list, name='item_list'),
        path('item/create/', views.item_create, name='item_create'),
        path('item/<int:pk>/', views.item_detail, name='item_detail'),
        path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
        path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    ]
    ```

1. <strong>Views</strong>: Implement the views for each of the CRUD operations in <code>views.py</code>.

    ```python
    # views.py
    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Item

    def item_list(request):
        items = Item.objects.all()
        return render(request, 'item_list.html', {'items': items})

    def item_detail(request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'item_detail.html', {'item': item})

    def item_create(request):
        if request.method == "POST":
            name = request.POST.get('name')
            description = request.POST.get('description')
            item = Item(name=name, description=description)
            item.save()
            return redirect('item_detail', pk=item.pk)
        return render(request, 'item_form.html', {})

    def item_edit(request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.method == "POST":
            item.name = request.POST.get('name')
            item.description = request.POST.get('description')
            item.save()
            return redirect('item_detail', pk=item.pk)
        return render(request, 'item_form.html', {'item': item})

    def item_delete(request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.method == "POST":
            item.delete()
            return redirect('item_list')
        return render(request, 'item_confirm_delete.html', {'item': item})

    ```

1. <strong>Templates</strong>: Create the necessary templates.
    - <strong>item_list.html</strong>:

        ```html
        {% for item in items %}
            <a href="{% url 'item_detail' item.pk %}">{{ item.name }}</a>
            <a href="{% url 'item_edit' item.pk %}">Edit</a>
            <a href="{% url 'item_delete' item.pk %}">Delete</a>
        {% endfor %}
        <a href="{% url 'item_create' %}">Create New Item</a>
        ```

    - <strong>item_detail.html</strong>:

        ```html
        <h1>{{ item.name }}</h1>
        <p>{{ item.description }}</p>
        <a href="{% url 'item_edit' item.pk %}">Edit</a>
        <a href="{% url 'item_delete' item.pk %}">Delete</a>
        ```

    - <strong>item_form.html</strong>:

        ```html
        <form method="post">
            {% csrf_token %}
            Name: <input type="text" name="name" value="{{ item.name|default:'' }}">
            Description: <textarea name="description">{{ item.description|default:'' }}</textarea>
            <input type="submit" value="Save">
        </form>
        ```

    - <strong>item_confirm_delete.html</strong>:

        ```html
        <h1>Are you sure you want to delete {{ item.name }}?</h1>
        <form method="post">
            {% csrf_token %}
            <input type="submit" value="Confirm Delete">
        </form>
        <a href="{% url 'item_list' %}">Cancel</a>
        ```

1. <strong>Run Migrations</strong>:
Remember to make migrations and migrate your database after creating the model.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

1. <strong>Test</strong>: Run your Django development server and navigate to the defined URLs to test your CRUD operations.

    ```bash
    python manage.py runserver
    ```

Now you can visit the specified URLs in your browser to Create, Read, Update, and Delete items using the Django templates without Model Forms.

Note: On each file you create, if you want to be able to use bootstrap, any styling, and to use the consistant navbar, add this to the top of our templates

```html
{% extends "adminapp/base/index.html" %}
```

That page is where the site structure is located.
