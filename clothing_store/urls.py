from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('my_app.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('wish_list/', include('wish_list.urls')),
    path('review/', include('review.urls')),
    path('purchase/', include('purchase.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)