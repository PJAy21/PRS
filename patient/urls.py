from django.urls import path
from .views import add_patient, update_patient, list_patient, delete_patient

urlpatterns = [
    path('', list_patient, name='list_pat'),
    path('add/', add_patient, name='add_pat'),
    path('update/<int:pk>', update_patient, name='update_pat'),
    path('delete/<int:pk>', delete_patient, name='delete_pat'),
]