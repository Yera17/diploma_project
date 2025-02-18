from django.urls import path
from . import views

app_name = 'purchase'

urlpatterns = [
    path('<int:purchase_id>/', views.purchase, name='purchase'),
    path('make_purchase', views.make_purchase, name='make_purchase'),
    path('cancel/<int:purchase_id>/', views.cancel_purchase, name='cancel'),
    path('buy/<int:purchase_id>/', views.buy, name='buy'),
]
