from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contacts/', views.contacts, name='contacts'),
    path('predications/', views.predications, name='predications'),
    path('agenda/', views.agenda, name='agenda'),
    path('agenda/<int:evenement_id>/', views.evenement_detail, name='evenement_detail'),
    path('predications/<int:predication_id>/', views.predication_detail, name='predication_detail'),
]
