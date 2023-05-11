from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets, permissions, authentication, views, response, status
from rest_framework.authtoken.models import Token

from SurfWallet.serializers.user_serializer import UserSerializer
from SurfWallet.models.user import CustomUser


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, ]
    authentication_classes = [authentication.BasicAuthentication, ]


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # We get the credentials and authenticate the user
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username is None or password is None:
            return response.Response({'message': 'Please provide both username and password'},
                                     status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return response.Response({'message': 'Wrong username or password'},
                                     status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        # We add the token info to the request if everything is fine
        if user:
            # para loguearse una sola vez
            login(request, user)
            return response.Response({'message': 'Correct user and password'}, status=status.HTTP_200_OK)
            # return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Return a server error if something goes wrong and gets to this line
        return response.Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        # Delete the token from the request
        request.user.auth_token.delete()
        logout(request)
        # Return an OK message
        return response.Response({'message': 'Logged out correctly!'}, status=status.HTTP_200_OK)