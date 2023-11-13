# Generated by Django 4.2.3 on 2023-10-25 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userlicense'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='justin.ferwerda@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercounty',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counties', to='api.user'),
        ),
        migrations.AlterField(
            model_name='userspecialization',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='api.user'),
        ),
    ]
