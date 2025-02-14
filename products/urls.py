from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:product_id>/', views.detail, name='detail'),
    path('<str:category_name>/', views.category_products, name='category'),
]
