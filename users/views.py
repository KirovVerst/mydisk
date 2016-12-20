from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from users.signals import *


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
