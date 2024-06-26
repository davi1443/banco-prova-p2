from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),
    path('eventos/', views.eventos_list, name='eventos_list'),
    path('eventos/create/', views.eventos_create, name='eventos_create'),
    path('eventos/<int:pk>/update/', views.eventos_update, name='eventos_update'),
    path('eventos/<int:pk>/delete/', views.eventos_delete, name='eventos_delete'),
]