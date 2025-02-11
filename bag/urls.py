from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('', views.bag, name='bag'),
    path('delete_bag_item/<int:bag_item_id>/', views.delete_bag_item, name='delete_bag_item'),
]
