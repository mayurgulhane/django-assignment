# Generated by Django 5.0.4 on 2024-04-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp_secret_key',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
