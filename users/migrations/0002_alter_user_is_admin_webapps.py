# Generated by Django 4.1.6 on 2023-02-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin_WebApps',
            field=models.BooleanField(default=True),
        ),
    ]