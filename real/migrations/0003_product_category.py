# Generated by Django 3.0.5 on 2020-05-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0002_auto_20200504_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.CharField(choices=[('Villa', 'Villa'), ('Banglov', 'Banglov'), ('Land', 'Land'), ('Apartment', 'Apartment'), ('Office', 'Office'), ('Warehouse', 'Warehouse')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]