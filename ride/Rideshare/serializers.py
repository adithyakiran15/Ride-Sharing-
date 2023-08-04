from .models import Ride
from rest_framework import serializers
from django.contrib.auth import get_user_model

class rideserializers(serializers.ModelSerializer):
    class Meta:
        model=Ride
        fields = ['id','rider','driver','status','pickup_location','drop_location','created_at','updated_at','completed']


class Userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self, validated_data):
        user=get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')

