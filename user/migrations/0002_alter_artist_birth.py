# Generated by Django 4.0.2 on 2022-02-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birth',
            field=models.DateField(null=True, verbose_name='출생년도'),
        ),
    ]
