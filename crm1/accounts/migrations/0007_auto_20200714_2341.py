# Generated by Django 3.0.8 on 2020-07-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
    ]
