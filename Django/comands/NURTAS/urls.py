from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('player', views.player, name='player'),
    path('add_player/', views.add_player, name='add_player'),
    path('delete_player/<int:id>/', views.delete_player, name='delete_player'),
    path('details/<int:id>', views.details, name='details'),
    path("edit_player/<int:id>/", views.edit_player, name='edit_player'),
]
