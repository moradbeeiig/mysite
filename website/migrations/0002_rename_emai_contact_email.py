# Generated by Django 3.2.19 on 2023-06-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Emai',
            new_name='Email',
        ),
    ]