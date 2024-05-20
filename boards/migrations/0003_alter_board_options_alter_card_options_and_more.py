# Generated by Django 5.0.6 on 2024-05-15 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_card_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'Tableau', 'verbose_name_plural': 'Tableaux'},
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Carte', 'verbose_name_plural': 'Cartes'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Commentaire', 'verbose_name_plural': 'Commentaires'},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'Liste', 'verbose_name_plural': 'Listes'},
        ),
        migrations.AddField(
            model_name='board',
            name='type',
            field=models.CharField(choices=[('PROJ', 'Tableau de Projet'), ('KAN', 'Kanban'), ('TEAM', "Tableau de Bord d'équipe")], default='PROJ', max_length=5, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='board',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL, verbose_name='Propriétaire'),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Texte'),
        ),
        migrations.AlterField(
            model_name='list',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='boards.board', verbose_name='Tableau'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
    ]