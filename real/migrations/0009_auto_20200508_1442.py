# Generated by Django 3.0.5 on 2020-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0008_auto_20200508_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qfield',
            name='owner_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='qfield',
            name='your_email',
            field=models.EmailField(max_length=254),
        ),
    ]