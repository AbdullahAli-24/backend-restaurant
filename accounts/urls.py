from django.urls import path
from .views import all_users


urlpatterns = [
    path('acounts/',all_users)
]
    