# Generated by Django 4.1.3 on 2023-05-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_rename_memberdetails_memberdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="memberdetail",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
    ]
