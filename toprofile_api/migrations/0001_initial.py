# Generated by Django 4.0 on 2024-06-12 12:36

from django.db import migrations, models
import django.db.models.deletion
import toprofile_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.AboutUs.upload_to)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AgentMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.AgentMember.upload_to)),
                ('facebook_link', models.URLField(null=True)),
                ('instagram_link', models.URLField(null=True)),
                ('email_link', models.URLField(null=True)),
                ('twitter_link', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('body', models.TextField()),
                ('author_name', models.CharField(max_length=300, null=True)),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.Blog.upload_to)),
                ('reading_time', models.CharField(max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('sub_heading', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FillContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('sub_heading', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.HeroSection.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.OurTeam.upload_to)),
                ('first_name', models.CharField(max_length=500, null=True)),
                ('last_name', models.TextField(max_length=500, null=True)),
                ('postion', models.TextField(max_length=500, null=True)),
                ('facebook_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('email_link', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivatePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.TextField()),
                ('address', models.CharField(max_length=500, null=True)),
                ('land_space', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TermsOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('comment', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=toprofile_api.models.Testimony.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=toprofile_api.models.ImageAsset.upload_to)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toprofile_api.propertylisting')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(null=True)),
                ('sub_heading', models.CharField(max_length=500)),
                ('agent', models.ManyToManyField(related_name='agents', to='toprofile_api.AgentMember')),
            ],
        ),
    ]
