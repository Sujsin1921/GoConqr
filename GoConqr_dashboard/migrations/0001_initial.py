# Generated by Django 4.0 on 2022-01-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=190)),
            ],
        ),
    ]
