# Generated by Django 5.0 on 2024-01-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_comment_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, default="default_image.jpg", null=True, upload_to="images/"
            ),
        ),
    ]
