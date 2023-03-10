# Generated by Django 4.0.5 on 2022-12-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_rename_evaluationdays_setting_evaluation_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='evaluation_score',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='setting',
            name='initial_score',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='setting',
            name='referral_score',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]
