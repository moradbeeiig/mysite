# Generated by Django 3.2.19 on 2023-07-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]