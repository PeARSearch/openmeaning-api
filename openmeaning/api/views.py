from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from openmeaning.api.serializers import UserSerializer, GroupSerializer, VectorSerializer
from openmeaning.api.models import Vector

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class VectorViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows vectors to be viewed or edited.
  """
  queryset = Vector.objects.all()
  serializer_class = VectorSerializer

#class VectorInstanceView(viewsets.ModelViewSet):
#  """
#  Returns a single vector.
#  """
#  model = Vector
#  serializer_class = VectorSerializer
