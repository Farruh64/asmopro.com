from rest_framework import serializers
from .models import *

class ServiceSerializers(serializers.ModelSerializer):
    class Meta():
        model = Service
        fields = '__all__'

class CallSerializers(serializers.ModelSerializer):
    class Meta():
        model = Call
        fields = '__all__'

class PortfolioSerializers(serializers.ModelSerializer):
    class Meta():
        model = Portfolio
        fields = '__all__'               

class MassageSerializers(serializers.ModelSerializer):
    class Meta():
        model = Massage
        fields = '__all__' 

class OtzivSerializers(serializers.ModelSerializer):
    class Meta():
        model = Otziv
        fields = '__all__'    

class NewsSerializers(serializers.ModelSerializer):
    class Meta():
        model = News
        fields = '__all__'                  
