# Generated by Django 4.1.1 on 2022-10-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_header_image_alter_post_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/images'),
        ),
    ]
