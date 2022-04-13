from rest_framework import serializers
from .models import *

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['context']
