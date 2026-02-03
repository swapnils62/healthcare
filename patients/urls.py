from django.urls import path
from patients import views

urlpatterns = [
    path('',views.PatientcretaView.as_view()),
    path('<int:id>/',views.PatientdetailView2.as_view()),
]

