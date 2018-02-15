# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0018_auto_20180117_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='has_newsletter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_http_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_http_mailfield',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_http_url',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_mail_from',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_mail_subject',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_mail_to',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='petition',
            name='newsletter_subscribe_method',
            field=models.CharField(blank=True, choices=[('MAIL', 'MAIL'), ('POST', 'POST'), ('GET', 'GET')], default='MAIL', max_length=4),
        ),
    ]