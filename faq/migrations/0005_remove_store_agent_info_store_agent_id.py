# Generated by Django 5.0.7 on 2024-08-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_store_agent_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='agent_info',
        ),
        migrations.AddField(
            model_name='store',
            name='agent_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
