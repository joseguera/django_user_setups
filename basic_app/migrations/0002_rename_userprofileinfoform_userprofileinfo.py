# Generated by Django 3.2.5 on 2021-08-12 19:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfoForm',
            new_name='UserProfileInfo',
        ),
    ]
