from os import name
from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):



    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(email = validated_data['email'],first_name=validated_data['first_name'],username=validated_data['username'],
                                        address = validated_data['address'])
        user.set_password(validated_data['password'])
        user.save()
        return user


    # def validate(self, data):
    #     if data['password'] != data['password1']:
    #         raise serializers.ValidationError({"error":"Password does not match"})

    # d
        

