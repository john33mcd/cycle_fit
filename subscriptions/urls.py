from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('nutrition_plan/', views.get_nutrition, name='nutrition_plan'),
    path('annual_cycle_fit_plan/', views.get_nutrition, name='annual_cycle_fit_plan'),
    path('<subscription_id>', views.subscription_detail, name='subscription_detail'),
]
