from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_session, name='home'),
    path('<str:session_id>/', views.session_view, name='session'),
    path('hook/<str:session_id>/', views.hook_receiver),
]