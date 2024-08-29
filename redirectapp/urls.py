from django.urls import path
from .views import redirect_view, loading_view

urlpatterns = [
    path('loading/', loading_view, name='loading_view'),
    path('redirect/<str:encrypted_url>/', redirect_view, name='redirect_view'),
]
