from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostView, 'post')

urlpatterns = [
    
    path('api/', include(router.urls)),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
