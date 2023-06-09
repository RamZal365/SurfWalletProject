"""
URL configuration for SurfWalletProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from SurfWallet.views.spot import SpotViewSet
from SurfWallet.views.surfboard import SurfBoardViewSet
from SurfWallet.views.user import UserViewSet, LoginView, LogoutView, SignupViewSet
from SurfWallet.views.wetsuit import WetSuitViewSet

router = routers.DefaultRouter()
router.register('surfboards', SurfBoardViewSet)
router.register('wetsuits', WetSuitViewSet)
router.register('spots', SpotViewSet)
router.register('users', UserViewSet)
router.register('signup', SignupViewSet, basename="signup")

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
] + router.urls
