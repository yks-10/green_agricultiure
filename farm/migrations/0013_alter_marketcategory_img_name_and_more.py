# Generated by Django 4.1.3 on 2022-12-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0012_marketform_trade_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketcategory',
            name='img_name',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='marketform',
            name='prod_image',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
