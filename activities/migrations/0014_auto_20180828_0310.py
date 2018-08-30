# Generated by Django 2.0.7 on 2018-08-28 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0013_auto_20180828_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age_class',
            name='age_class',
            field=models.CharField(max_length=100, unique=True, verbose_name="Classe d'age"),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=100, unique=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nom'),
        ),
    ]