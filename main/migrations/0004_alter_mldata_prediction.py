# Generated by Django 4.1.2 on 2022-11-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mldata_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mldata',
            name='prediction',
            field=models.IntegerField(null=True),
        ),
    ]