# Generated by Django 4.0.4 on 2022-04-18 02:53

import candidate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_alter_aptitude_name_alter_candidatestatus_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='InterviewDate',
            field=models.DateField(blank=True, null=True, validators=[candidate.models.validdate]),
        ),
    ]
