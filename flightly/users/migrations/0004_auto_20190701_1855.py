# Generated by Django 2.2.2 on 2019-07-01 18:55

from django.db import migrations, models
import django_cryptography.fields
import flightly.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190701_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightlyuser',
            name='photograph',
            field=django_cryptography.fields.encrypt(models.ImageField(default='img/None', upload_to=flightly.users.models.user_directory_path, verbose_name='Passport Photograph')),
        ),
    ]