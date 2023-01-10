# Generated by Django 4.1.3 on 2022-11-10 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_champfav_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.career'),
        ),
    ]
