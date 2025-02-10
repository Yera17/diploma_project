from django.urls import path
from . import views

app_name = 'wish_list'

urlpatterns = [
    path('', views.wish_list, name='wish_list'),
    path('add_to_wish_list/<int:product_id>/', views.add_to_wish_list, name='add_to_wish_list'),
    path('remove_from_wish_list/<int:wish_list_item_id>', views.remove_from_wish_list, name='remove_from_wish_list'),
]