# Generated by Django 4.1.3 on 2022-12-11 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0010_alter_marketcategory_img_name_marketform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketform',
            old_name='seller',
            new_name='user',
        ),
    ]
