# boards/models.py

from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    PROJECT = 'PROJ'
    KANBAN = 'KAN'
    TEAM_BOARD = 'TEAM'
    AGILE_BOARD = 'AGILE'
    TRACK_BUG = 'BUG'

    BOARD_TYPE_CHOICES = [
        (PROJECT, 'Conduite de Projet'),
        (KANBAN, 'Modèle Kanban'),
        (TEAM_BOARD, 'Tableau de Bord d\'équipe'),
        (AGILE_BOARD, 'Tableau Agile'),
        (TRACK_BUG, 'Traçage des anomalies'),
    ]

    name = models.CharField(max_length=100, verbose_name='Nom')
    owner = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE, verbose_name='Propriétaire')
    type = models.CharField(max_length=5, choices=BOARD_TYPE_CHOICES, default=PROJECT, verbose_name='Type')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    date_deleted = models.DateTimeField(blank=True, null=True, verbose_name='Date de suppression')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tableau'
        verbose_name_plural = 'Tableaux'


class List(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE, verbose_name='Tableau')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Liste'
        verbose_name_plural = 'Listes'


class Card(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titre')
    description = models.TextField(blank=True, null=True)
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_board(self):
        return self.list.board.name

    get_board.short_description = 'Board'

    class Meta:
        ordering = ['order']  # on trie par position
        verbose_name = 'Carte'
        verbose_name_plural = 'Cartes'


class Comment(models.Model):
    text = models.TextField(verbose_name='Texte')
    card = models.ForeignKey(Card, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'
