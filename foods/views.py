
from rest_framework.decorators import api_view, permission_classes
from foods.models import Food, Category
from foods.serializers import FoodSerializer, CategorySerializer
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_foods(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

    
@api_view(['GET'])
def List_Categories(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)
  