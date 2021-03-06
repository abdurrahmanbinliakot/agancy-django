# Generated by Django 3.1 on 2020-08-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, max_length=20)),
                ('about_heading', models.TextField(max_length=30)),
                ('about_description', models.TextField(max_length=200)),
                ('about_image', models.ImageField(upload_to='about_images')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.TextField(max_length='50')),
                ('client_url', models.URLField()),
                ('client_logo', models.ImageField(upload_to='clients_url')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_heading', models.TextField(max_length=50)),
                ('portfolio_sub_heading', models.TextField(max_length=100)),
                ('portfolio_image', models.ImageField(upload_to='portfolio_images')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_heading', models.TextField(max_length=30)),
                ('service_description', models.TextField(max_length=100)),
                ('service_icon', models.CharField(choices=[('laptop', 'laptop'), ('camera', 'camera'), ('book', 'book')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('designation', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='team_member_photo')),
                ('facebook_profile', models.URLField()),
                ('twitter_profile', models.URLField()),
                ('linkedin_profile', models.URLField()),
            ],
        ),
    ]
