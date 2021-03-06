# Generated by Django 2.1.5 on 2019-03-31 22:02

from django.db import migrations
from django.utils.text import slugify


def create_org_slugs(apps, schema_editor):
    Organization = apps.get_model('petition', 'Organization')
    for o in Organization.objects.all():
        if not o.slugname:
            slugtext = slugify(o.name)[:200]
            o.slugname = slugtext
            o.save()


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0024_petition_slugs'),
    ]

    operations = [
        migrations.RunPython(create_org_slugs, migrations.RunPython.noop)
    ]
