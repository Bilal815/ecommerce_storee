# Generated by Django 3.2.12 on 2022-04-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20220419_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='product/images/'),
        ),
    ]
