# Generated by Django 3.2.12 on 2022-04-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20220419_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='range',
        ),
        migrations.AddField(
            model_name='product',
            name='age_range',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Ludwin Dieter', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='frequency',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='French Designer', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='oxygen',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pd_range',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='presc_range',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type_tag',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='usage',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='water',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='frame_material',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='lens_material',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shape',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uv',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
