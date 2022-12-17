from django.urls import path
from . import views

urlpatterns = [
    path('PurchasedBooks', views.getPurchasedBooks),
    path('PurchasedBooksD/<str:bookName>', views.getBooksDetails),
    path('purchase', views.purchaseBook)

]
