# Generated by Django 5.0.6 on 2024-05-20 00:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_alter_board_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['order'], 'verbose_name': 'Carte', 'verbose_name_plural': 'Cartes'},
        ),
        migrations.AddField(
            model_name='board',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de creation'),
            preserve_default=False,
        ),
    ]
