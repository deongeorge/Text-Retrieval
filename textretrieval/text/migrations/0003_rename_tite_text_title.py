# Generated by Django 3.2.4 on 2021-06-26 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_auto_20210626_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='tite',
            new_name='title',
        ),
    ]
