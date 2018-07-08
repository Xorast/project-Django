# Generated by Django 2.0.7 on 2018-07-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20180708_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='noimage.jpg', upload_to='images/events'),
        ),
    ]
