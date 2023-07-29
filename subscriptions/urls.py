from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('<subscription_id>', views.subscription_detail, name='subscription_detail'),
]