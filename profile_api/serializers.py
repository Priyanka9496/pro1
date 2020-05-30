from rest_framework import serializers
from django.db import models


class HelloSerializer(serializers.Serializer):

    name= serializers.CharField(max_length=10)
