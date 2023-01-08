# Generated by Django 4.1.3 on 2022-11-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0004_agriculturalscraps_alter_userdetails_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmersNotebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(blank=True, max_length=50, null=True)),
                ('note_date', models.DateTimeField(auto_now_add=True)),
                ('note_description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Farmers Note',
                'verbose_name_plural': 'Farmers Notes',
                'ordering': ['-pk'],
            },
        ),
        migrations.AlterField(
            model_name='agriculturalscraps',
            name='scrap_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]