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
from rest_framework_simplejwt.views import TokenRefreshView
from auth import views as viewsAuth
from django.conf import settings
from django.conf.urls.static import static

router =routers.DefaultRouter()
router.register('rooms',views.HotelRoomViewSet)
router.register('reviews',views.ReviewViewSet)
router.register('reservations',views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',viewsAuth.MyObtainTokenPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/', viewsAuth.RegisterView.as_view(), name='auth_register'),
    path('accomodation/',include(router.urls)),
    path('accomodation/user_reservations/', views.get_user_reservations),
    path('accomodation/reservation_dates/<int:room>/', views.get_reservation_dates),
    path('upload/', views.ImageViewSet.as_view(), name='upload'),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
