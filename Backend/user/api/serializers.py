from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id')



class CreateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()


    def validate_username(self, usuario):
        if User.objects.filter(username=usuario).exists():
            raise serializers.ValidationError('Usuário Indisponível!')
        return usuario

    def create(self, validated_data):
        self.instance = User.objects.create_user(first_name=validated_data['first_name'],
                                                 last_name=validated_data['last_name'],
                                                 username=validated_data['username'],
                                                 password=validated_data['password'], )

        return self.instance
