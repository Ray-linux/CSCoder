# Generated by Django 3.2.12 on 2022-06-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='thumbnails/'),
        ),
    ]
