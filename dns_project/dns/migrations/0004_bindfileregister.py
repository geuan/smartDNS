# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns', '0003_bindconfigview_readable_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BindFileRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='文件路径')),
                ('file_type', models.IntegerField(choices=[(0, 'zone file'), (1, 'iplist config file'), (2, 'named.conf')], default=0, verbose_name='文件类型')),
                ('is_deleted', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否已删除')),
            ],
        ),
    ]