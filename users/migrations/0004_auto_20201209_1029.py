# Generated by Django 3.1.2 on 2020-12-09 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='user_mail_id',
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
