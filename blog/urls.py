from django.urls import path, include
import .views 

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
]    
