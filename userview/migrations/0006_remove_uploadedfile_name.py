# Generated by Django 4.1.2 on 2022-12-23 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userview", "0005_uploadedfile_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="uploadedfile", name="name",),
    ]
