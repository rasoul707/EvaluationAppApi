# Generated by Django 4.0.5 on 2022-08-02 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_remove_software_evaluations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='software',
            options={'ordering': ('-is_active', 'name')},
        ),
    ]