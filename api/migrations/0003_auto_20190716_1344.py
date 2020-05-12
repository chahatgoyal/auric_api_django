# Generated by Django 2.2.2 on 2019-07-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_city_group_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.City'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location'),
        ),
    ]
