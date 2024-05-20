# boards/admin.py

from django.contrib import admin
from .models import Board, List, Card, Comment


class ListInline(admin.TabularInline):
    model = List
    extra = 1


class CardInline(admin.TabularInline):
    model = Card
    extra = 1


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name', 'owner__username')
    inlines = [ListInline]
    verbose_name_plural = 'Tableau de bord'


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'board')
    search_fields = ('name', 'board__name')
    inlines = [CardInline]
    verbose_name_plural = 'Listes'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'get_board')
    search_fields = ('title', 'list__name')
    verbose_name_plural = 'Cartes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'card', 'author', 'created_at')
    search_fields = ('text', 'card__title', 'author__username')
    list_filter = ('created_at', 'author')
    verbose_name_plural = 'Commentaires'
