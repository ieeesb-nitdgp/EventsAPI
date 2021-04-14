from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from feedbacks import views

router = routers.DefaultRouter()
router.register(r'feedbacks', views.FeedbackView, 'feedback')

urlpatterns = [
    
    path('api/', include(router.urls)),
]
