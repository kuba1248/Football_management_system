# Generated by Django 3.1.2 on 2020-12-12 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201212_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='stadium_id',
        ),
        migrations.DeleteModel(
            name='stadium',
        ),
    ]