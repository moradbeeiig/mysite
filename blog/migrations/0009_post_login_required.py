# Generated by Django 3.2.19 on 2023-07-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]