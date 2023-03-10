# Generated by Django 4.1.3 on 2023-01-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0024_cropcultivation_alter_scientist_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalHusbandry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_name', models.CharField(blank=True, max_length=100, null=True)),
                ('husbandry', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'Animal Husbandry',
                'verbose_name_plural': 'Animals Husbandry',
                'ordering': ['-pk'],
            },
        ),
    ]
