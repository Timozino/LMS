# Generated by Django 3.2.16 on 2022-11-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]