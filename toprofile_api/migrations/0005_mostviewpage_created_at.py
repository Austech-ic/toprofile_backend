# Generated by Django 4.0 on 2024-08-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toprofile_api', '0004_blog_slug_propertylisting_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostviewpage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
