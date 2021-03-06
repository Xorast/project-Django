# Generated by Django 2.0.7 on 2018-08-26 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20180826_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_animation_slot',
            name='period',
        ),
        migrations.AddField(
            model_name='activity_animation',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Animation', to='activities.Period'),
        ),
        migrations.AlterField(
            model_name='activity_animation_slot',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Slot', to='activities.Level'),
        ),
    ]
