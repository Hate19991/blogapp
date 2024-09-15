from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('note/write/', views.write, name='write_note'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('note/update/<int:pk>/', views.update_note, name='update_note'),
    path('index/delete/<int:pk>/', views.delete_note, name='delete_note'),
]
