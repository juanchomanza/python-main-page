# Generated by Django 4.1.3 on 2022-11-02 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_career'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='name',
            new_name='user',
        ),
    ]
