from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/', views.edit, name='edit'),
    path('home/', views.submitEdit, name='submitEdit'),
    path('home1/', views.delete, name='delete'),
    path('add/', views.addEmployee, name='addEmployee'),
    path('home2/', views.submitAddEmployee, name='submitAddEmployee'),
]



# urlpatterns = [
#     path('', views.home, name='home'),
#     path('edit/', views.edit, name='edit'),
#     path('home/', views.submitEdit, name='submitEdit'),
#     path('delete/', views.delete, name='delete'),
#     path('add/', views.addEmployee, name='addEmployee'),
#     path('addEmp/', views.submitAddEmployee, name='submitAddEmployee'),
# ]

