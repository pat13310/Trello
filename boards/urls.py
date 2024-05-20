# boards/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ajout de la page d'accueil
    path('update_card_order/', views.update_card_order, name='update_card_order'),
    path('create_board/', views.create_board, name='create_board'),
    path('create_list/<int:board_pk>/', views.create_list, name='create_list'),
    path('create_card/<int:list_pk>/', views.create_card, name='create_card'),
    path('boards/<int:pk>/', views.board_detail, name='board_detail'),  # Ajout de la vue de détail du tableau
    path('login/', views.login_view, name='login'),  # Ajoutez cette route pour la vue login
    path('logout/', views.logout_view, name='logout'),
    path('list_board/', views.list_board, name='list_board'),
    path('create_model/<str:model_type>/', views.create_model, name='create_model'),
    path('remove_board/<int:pk>/', views.remove_board, name='remove_board'),

    # JSON

    # Board
    path('edit_board/', views.edit_board, name='edit_board'),
    path('delete_board/', views.delete_board, name='delete_board'),

    # List
    path('edit_list/', views.edit_list, name='edit_list'),

    # Card
    path('edit_card/', views.edit_card, name='edit_card'),
    path('update-card-order/', views.update_card_order, name='update_card_order'),

]
