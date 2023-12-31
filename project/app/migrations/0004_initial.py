# Generated by Django 4.2.2 on 2023-06-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phonenumber', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
