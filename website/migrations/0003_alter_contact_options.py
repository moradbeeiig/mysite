# Generated by Django 3.2.19 on 2023-06-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_emai_contact_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
