from django.urls import path
from . import views

urlpatterns = [
    path('',views.benim,name='profile'),
    path('paylas',views.paylas,name='paylas')

]
