from .models import *
from rest_framework import serializers
from .models import *

class feedBack_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_FeedBack
        fields = '__all__'