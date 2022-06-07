from django.urls import path

from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # Home
    path('contato/', contato)  # Home
]
