# Generated by Django 2.0.7 on 2019-01-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181008_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/events/', verbose_name='PDF'),
        ),
    ]
