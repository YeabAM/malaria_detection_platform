# Generated by Django 4.0.4 on 2022-05-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final_Project', '0002_rename_credentials_credential_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.EmailField(default=' ', max_length=100),
        ),
    ]
