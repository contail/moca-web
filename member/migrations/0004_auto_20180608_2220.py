# Generated by Django 2.0.6 on 2018-06-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20180608_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]