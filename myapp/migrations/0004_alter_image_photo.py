# Generated by Django 4.1.7 on 2023-03-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_image_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="photo",
            field=models.FileField(upload_to="myimage"),
        ),
    ]
