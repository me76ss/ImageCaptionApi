# Generated by Django 3.1.6 on 2021-02-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210201_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='image',
        ),
    ]
