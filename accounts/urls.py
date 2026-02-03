from django.urls import path
from accounts import views

urlpatterns = [
    path('register/',views.Regiterview.as_view()),
    path('login/',views.Loginview.as_view())
]
