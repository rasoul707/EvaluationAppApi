# Generated by Django 4.0.5 on 2022-12-07 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
        ('authentication', '0014_account_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='documents',
            field=models.ManyToManyField(related_name='documents', to='upload.image'),
        ),
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='avatar', to='upload.image'),
        ),
    ]
