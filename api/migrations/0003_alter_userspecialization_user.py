# Generated by Django 4.2.3 on 2023-07-17 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_specialization_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspecialization',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specialization', to='api.user'),
        ),
    ]