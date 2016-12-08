from django.contrib.auth.models import User, Group
from openmeaning.api.models import Vector
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')

class VectorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Vector
    fields = ('word', 'vector')
