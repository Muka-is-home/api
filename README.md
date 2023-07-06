# api
### Loading fixtures
You will need to first create two superusers:
```shell
python manage.py createsuperuser
```

After creating two superusers, you can load the fixtures:
```
python manage.py loaddata content_types states tags counties specializations user_types users user_specializations user_counties content_tags contents
```
