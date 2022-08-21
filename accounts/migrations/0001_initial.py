# Generated by Django 4.0.6 on 2022-07-16 15:20

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Username', models.CharField(max_length=20, verbose_name='username')),
                ('fname', models.CharField(blank=True, max_length=20, verbose_name='firstname')),
                ('lname', models.CharField(max_length=20, verbose_name='lastname')),
                ('bdate', models.DateField(verbose_name='birth date')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('about', models.TextField(default='', max_length=50, verbose_name='tell about youself')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_joined', models.DateField(auto_now=True, verbose_name='last joined')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('OBJECTS', django.db.models.manager.Manager()),
            ],
        ),
    ]
