# Generated by Django 4.0 on 2024-09-19 17:17

from django.db import migrations, models
import toprofile_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('toprofile_api', '0011_alter_blog_slug_alter_propertylisting_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourservices',
            name='image',
            field=models.ImageField(max_length=500, null=True, upload_to=toprofile_api.models.OurServices.upload_to),
        ),
    ]
