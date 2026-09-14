from django.urls import path
from .views import get_all_foods, List_Categories


urlpatterns = [
    path('', get_all_foods, name='food_list'),
    path('categories/', List_Categories, name='category_list'),
    # path('<int:food_id>/',food_detail, name='food_detail'),
]