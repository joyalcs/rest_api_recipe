# Generated by Django 4.2.4 on 2023-08-27 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
