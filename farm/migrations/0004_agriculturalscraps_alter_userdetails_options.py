# Generated by Django 4.1.3 on 2022-11-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_rename_name_userdetails_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriculturalScraps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap_title', models.CharField(blank=True, max_length=50, null=True)),
                ('scrap_description', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Agricultural Scrap',
                'verbose_name_plural': 'Agricultural Scraps',
                'ordering': ['-pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'ordering': ['-pk'], 'verbose_name': 'User Detail', 'verbose_name_plural': 'user Details'},
        ),
    ]
