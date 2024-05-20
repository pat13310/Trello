# boards/forms.py

from django import forms
from .models import Board, List, Card

from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'type']
        labels = {
            'name': 'Nom',
            'type': 'Type',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'p-2 mt-1 block w-full border-violet-500 rounded-md shadow-sm focus:border-indigo-100 focus:ring-indigo-100 sm:text-sm'
            }),
            'type': forms.Select(attrs={
                'class': 'p-2 mt-1 block w-full border-violet-500 rounded-md shadow-sm focus:border-indigo-100 focus:ring-indigo-100 sm:text-sm'
            }),
        }


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description']
