from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','firstname', 'lastname', 'email', 'password', 'facultyNum', 'created_at', 'user_type') 