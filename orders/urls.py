from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
    path('create/', views.create, name='order_create'),
    path('completed/', views.order_success, name='order_success')
]