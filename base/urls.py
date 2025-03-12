from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('bills', views.get_all_bills, name='bills'),
    path('payment', views.make_payment, name='payment'),
]