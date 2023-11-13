# Generated by Django 4.2.3 on 2023-10-17 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('body', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('purchase_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=200)),
                ('on_homepage', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('website', models.URLField()),
                ('bio', models.TextField()),
                ('company', models.CharField(max_length=55)),
                ('company_address', models.CharField(max_length=86)),
                ('company_phone', models.CharField(max_length=17)),
                ('contact_no', models.CharField(max_length=17)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('image', models.URLField()),
                ('active', models.BooleanField(blank=True, null=True)),
                ('ready_for_approval', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='UserSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.specialization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specialization', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.county')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_county', to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usertype'),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state'),
        ),
        migrations.CreateModel(
            name='ContentTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.content')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tag')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contenttype'),
        ),
    ]
