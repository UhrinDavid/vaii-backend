"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from accomodationApp import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router =routers.DefaultRouter()
router.register('rooms',views.HotelRoomViewSet)
router.register('reviews',views.ReviewViewSet)
router.register('reservations',views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('accomodation/',include(router.urls)),
    path('accomodation/user_reservations/<int:user>/', views.get_user_reservations),
    path('accomodation/reservation_dates/<int:room>/', views.get_reservation_dates),
]
