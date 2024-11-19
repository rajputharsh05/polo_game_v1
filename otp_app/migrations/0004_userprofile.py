# Generated by Django 4.2.6 on 2024-11-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0003_remove_otpmodel_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('country_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
