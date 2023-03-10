# Generated by Django 4.0.5 on 2023-02-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_account_bank_account_alter_account_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='account',
            name='evaluator_scores',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='is_verified'),
        ),
        migrations.AddField(
            model_name='account',
            name='score_freeze',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='stars',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='withdrawal_request',
            field=models.BooleanField(default=False),
        ),
    ]
