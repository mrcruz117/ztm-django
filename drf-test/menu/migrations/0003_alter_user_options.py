# Generated by Django 4.2.6 on 2023-10-26 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name_plural': 'Users'},
        ),
    ]
