# Generated by Django 3.1.4 on 2020-12-07 23:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adress',
            new_name='Address',
        ),
    ]