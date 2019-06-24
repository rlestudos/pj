from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from user.api.serializers import CreateUserSerializer, UserSerializer
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from user.models import User


class CreateUserAPI(ViewSet):
    permission_classes = (AllowAny,)

    def get_serializer(self, *args, **kwargs):
        return CreateUserSerializer(*args, **kwargs)

    def post(self, request, format=None):
        user = self.get_serializer(data=request.data)
        if user.is_valid(True):
            user = user.save()
            token = Token.objects.create(user=user)
            return Response('Retorno: Usuário Criado!', status=status.HTTP_201_CREATED)


class LoginUserAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginUserAPI, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(auth_token=response.data['token'])
        return Response(
            {'token': token.key, 'id': token.user_id, 'nome': user.first_name})
