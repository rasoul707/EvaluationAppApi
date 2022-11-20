# Generated by Django 4.0.5 on 2022-08-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_remove_account_can_add_evaluation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_level',
            field=models.CharField(choices=[('level1', 'Level 1'), ('level2', 'Level 2'), ('level3', 'Level 3')], default='level1', max_length=100),
        ),
    ]