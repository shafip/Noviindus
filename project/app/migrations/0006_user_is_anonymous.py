# Generated by Django 4.2.2 on 2023-06-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_anonymous',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
