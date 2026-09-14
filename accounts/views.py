from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def all_users(request):
    user=User.objects.filter(username='ali').count()
    print(user)
    data=User.objects.all()
    serializer=UserSerializer(data,many=True)
    return Response(serializer.data)