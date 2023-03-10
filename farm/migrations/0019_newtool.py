# Generated by Django 4.1.3 on 2023-01-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0018_alter_marketform_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('tools_img', models.CharField(blank=True, max_length=3000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'New Tool',
                'verbose_name_plural': 'New Tools',
                'ordering': ['-pk'],
            },
        ),
    ]
