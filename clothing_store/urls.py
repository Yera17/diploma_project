from django.contrib import admin
from django.urls import path, include

from my_app.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('products/', include('products.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
