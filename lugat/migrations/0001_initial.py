# Generated by Django 4.2.8 on 2023-12-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=128)),
                ('uzbek', models.CharField(max_length=128)),
            ],
        ),
    ]
