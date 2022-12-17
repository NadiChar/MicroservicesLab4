from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.getBooks),
    path('addBook/', views.addBook),
    path('book/<int:id>', views.getBookByID),
    path('bookN/<str:bookName>', views.getBookByName),

]

