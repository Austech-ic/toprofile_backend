# Generated by Django 4.0 on 2024-08-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toprofile_api', '0008_blogviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogviews',
            name='count',
            field=models.BigIntegerField(default=1),
        ),
    ]
