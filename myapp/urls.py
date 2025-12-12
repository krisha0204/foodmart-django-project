from django.urls import path
from .views import login,food_view,add_food,edit,delete,index,register

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('food/', food_view, name='food'),
    path('add/', add_food, name='add_food'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    

]
