# Generated by Django 4.1.3 on 2022-11-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_remove_user_career_delete_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='career',
            field=models.CharField(default='yesdaddy', max_length=100),
        ),
    ]
