# boards/views.py
import os
import uuid

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.decorators.http import require_POST

from ProjectManager import settings
from .models import Board, List, Card
from .forms import BoardForm, ListForm, CardForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    boards = Board.objects.filter(owner=request.user)
    context = {
        'boards': boards,
        'board_type_choices': Board.BOARD_TYPE_CHOICES
    }
    return render(request, 'boards/home.html', context)


@login_required
def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/board_detail.html', {'board': board})


@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            return redirect('home')
    else:
        form = BoardForm()
    return render(request, 'boards/create_board.html', {'form': form})


@login_required
def create_list(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.board = board
            list.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = ListForm()

    return render(request, 'boards/create_list.html', {'form': form, 'board': board})


@login_required
def create_card(request, list_pk):
    list = List.objects.get(pk=list_pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.list = list
            card.save()
            return redirect('board_detail', pk=list.board.pk)
    else:
        form = CardForm()
    return render(request, 'boards/create_card.html', {'form': form, 'list': list})


@csrf_exempt
def update_card_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('card_id')
        new_list_id = data.get('new_list_id')
        new_position = data.get('new_position')

        card = Card.objects.get(id=card_id)
        new_list = List.objects.get(id=new_list_id)

        # Update the card's list and order
        card.list = new_list
        card.order = new_position
        card.save()

        return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'boards/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


@login_required
def list_board(request):
    boards = Board.objects.all()
    return render(request, 'boards/board_list.html', {'boards': boards})


@login_required
def create_model(request, model_type):
    # model_type = request.POST.get('model_type') or request.GET.get('model_type')
    custom_name = request.POST.get('board_name') or request.GET.get('board_name')

    # Charger la configuration des listes à partir du fichier JSON
    config_path = os.path.join(settings.BASE_DIR, 'boards_models.json')
    with open(config_path, 'r', encoding='utf-8') as config_file:
        lists_by_model_type = json.load(config_file)

    # Vérifier que le type de modèle est valide
    if model_type not in lists_by_model_type:
        return render(request, 'boards/home.html', {'message': 'Invalid model type'})
        # Générer un nom par défaut s'il n'y a pas de nom personnalisé

    if not custom_name:
        custom_name = f"{model_type}_Board_{uuid.uuid4().hex[:8]}"

    # Créer le board
    board = Board.objects.create(owner=request.user, type=model_type, name=custom_name)

    # Créer les listes associées
    for list_name in lists_by_model_type[model_type]:
        List.objects.create(board=board, name=list_name)

    # Sauvegarder le board
    board.save()

    # Rediriger vers la page de détails du board
    return redirect('board_detail', pk=board.pk)


@login_required
def remove_board(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('list_board')


@csrf_exempt
def edit_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('card_id')
        print("card_id", card_id)
        card_title = data.get('card_title')
        card = Card.objects.get(id=card_id)
        card.title = card_title
        card.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def delete_board(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board_id = data.get('board_id')
        board = Board.objects.get(id=board_id)
        board.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def edit_board(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board_id = data.get('board_id')
        board_name = data.get('board_name')
        board = Board.objects.get(id=board_id)
        board.name = board_name
        board.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def edit_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        liste = List.objects.get(id=data.get('list_id'))
        liste.name = data.get('list_name')
        liste.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
