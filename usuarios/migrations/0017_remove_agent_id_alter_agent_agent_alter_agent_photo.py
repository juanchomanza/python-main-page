# Generated by Django 4.1.3 on 2022-11-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_alter_agent_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='id',
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agent',
            name='photo',
            field=models.ImageField(null=True, upload_to='sap/files/agents'),
        ),
    ]
