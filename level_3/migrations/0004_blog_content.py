# Generated by Django 5.1.3 on 2024-11-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_3', '0003_alter_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]