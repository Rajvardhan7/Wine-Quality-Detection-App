# Generated by Django 4.1.2 on 2022-10-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mldata',
            name='age',
            field=models.IntegerField(),
        ),
    ]
