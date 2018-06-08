# Generated by Django 2.0.6 on 2018-06-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
