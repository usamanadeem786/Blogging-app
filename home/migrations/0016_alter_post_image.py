# Generated by Django 5.0 on 2024-01-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.FileField(null=True, upload_to="images/"),
        ),
    ]