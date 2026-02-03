from django.urls import path
from mappings import views

urlpatterns = [
    path('',views.DoctormapPatient.as_view()),
    path('<int:id>/',views.PDByPatientView.as_view()),
]

