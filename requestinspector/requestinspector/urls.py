from django.urls import path
from inspector import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:session_id>/', views.view_requests, name='view_requests'),
    path('hook/<str:session_id>/', views.receive_hook, name='receive_hook'),
]
