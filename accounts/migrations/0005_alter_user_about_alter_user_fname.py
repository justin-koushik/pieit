# Generated by Django 4.0.6 on 2022-07-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_about_alter_user_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=50, verbose_name='tell about youself'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=20, verbose_name='firstname'),
        ),
    ]
