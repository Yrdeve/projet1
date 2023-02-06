from django.urls import path
from projet1 import views

urlpatterns = [
    path('produit/', views.ProduitList.as_view()),
]