# Generated by Django 4.0 on 2022-01-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoConqr_dashboard', '0003_alter_course_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.CharField(max_length=300),
        ),
    ]
