
from django.urls import path
from . import views

urlpatterns = [
    # login
    path('', views.home, name=''),
    
    path('register', views.register, name='register'),
    
    path('login', views.login, name='login'),
    
    path('logout', views.logout, name='logout'),    
    
    #CRUD
    
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('create', views.create, name="create"), 
     
    path('update/<int:pk>', views.update, name='update'),
    
    path('record/<int:pk>', views.singular_record, name="record"),  
    
    path('delete/<int:pk>', views.delete, name="delete"),
    
    
]