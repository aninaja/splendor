from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.home, name='home'),

    # patient
    path('list', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('<int:pk>/disable/', views.patient_disable, name='patient_disable'),
    path('<int:pk>/patient-information', views.patient_info, name='patient_info'),
    path('<int:pk>/patient-renewal', views.patient_renewal, name='patient_renewal'),



]
