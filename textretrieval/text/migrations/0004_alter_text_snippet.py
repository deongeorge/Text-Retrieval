# Generated by Django 3.2.4 on 2021-06-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_rename_tite_text_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='snippet',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
