from django.urls import path
from . import views

urlpatterns = [
    # cesta (route) pro zobrazení úvodní stránky
    path('', views.index, name='index'),
    # cesta pro zobrazení výpisu všech filmů s využitím generické třídy FilmListView, název cesty je film_list
    path('films/', views.FilmListView.as_view(), name='film_list'),
    # cesta pro zobrazení výpisu detailu filmu s využitím funkce film_detail, název cesty je film_detail
    # součástí cesty je jeden parametr typu integer, předávaný jako atribut pk (umožní zadání primárního klíče filmu)
    path('films/<int:pk>', views.film_detail, name='film_detail'),
    # cesta pro zobrazení výpisu filmů určeného žánru s využitím funkce film_genre, název cesty je film_genre
    # součástí cesty je jeden parametr typu string, předávaný jako atribut genre (umožní zadání názvu žánru)
    path('films/genre/<str:genre>', views.film_genre, name='film_genre'),
]