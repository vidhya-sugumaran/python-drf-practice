from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('library/add_book/', views.add_book),
    path('library/list_books/', views.list_books),
    path('library/view_book/<id>', views.view_book),
    path('library/update_book/<id>', views.update_book),
    path('library/delete_book/<id>', views.delete_book),
]