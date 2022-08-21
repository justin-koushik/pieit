# Generated by Django 4.0.6 on 2022-07-26 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blog_likes_alter_blog_author_alter_blog_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateField(default=datetime.datetime(2022, 7, 26, 13, 1, 45, 852386, tzinfo=utc), editable=False, verbose_name='posted on'),
        ),
    ]
