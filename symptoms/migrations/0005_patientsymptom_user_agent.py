# Generated by Django 4.0.2 on 2022-04-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0004_patientsymptom_is_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsymptom',
            name='user_agent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
