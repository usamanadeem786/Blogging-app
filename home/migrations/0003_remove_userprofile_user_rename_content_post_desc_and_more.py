# Generated by Django 5.0 on 2024-01-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_post_comment_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="content",
            new_name="desc",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default="default_image.jpg", upload_to="images/"),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
