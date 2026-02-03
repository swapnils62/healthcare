from django.urls import path
from doctors import views

urlpatterns = [
    path('',views.Doctorcreateview.as_view()),
    path('<int:id>/',views.Doctordetailview.as_view()),
]