from rest_framework import serializers


class Userserializer(serializers.Serializer):
  id= serializers.IntegerField()(read_only=True)
  auth_token=serializers.CharField
  first_name= serializers.CharField()
  last_name= serializers.CharField()
  phonenumber= serializers.CharField()
  email=serializers.EmailField()
  