# Generated by Django 5.0.6 on 2024-05-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_board_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='date_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de suppression'),
        ),
    ]