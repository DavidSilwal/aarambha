# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='Published Date')),
                ('author', models.CharField(max_length=200)),
                ('author_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='our_event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='our_event',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='our_work',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
