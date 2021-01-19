from django.shortcuts import render
from accomodationApp.models import HotelRoom,Reservation,Review
from accomodationApp.serializers import HotelRoomSerializer,ReservationSerializer,ReservationSerializerBooked,ReviewSerializer,ReviewSerializerList,ReservationSerializerList
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
import jwt
from backend.settings import SECRET_KEY
from rest_framework.generics import ListAPIView
from rest_framework import status

# Create your views here.
class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = (AllowAny,)

    # Refer to https://stackoverflow.com/a/35987077/1677041
    permission_classes_by_action = {
        'create': permission_classes,
        'list': permission_classes,
        'retrieve': permission_classes,
        'update': permission_classes,
        'destroy': permission_classes,
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]

class HotelRoomViewSet(BaseModelViewSet):
    queryset=HotelRoom.objects.all()
    serializer_class=HotelRoomSerializer

    permission_action_classes = {
                'update': [IsAdminUser],
                'destroy': [IsAdminUser],
    } 



class ReviewViewSet(BaseModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAdminUser,]
    permission_action_classes = {
                'create': [IsAuthenticated],
                'list': [AllowAny],

    }

    def create(self, request, *args, **kwargs):
        request.data["userID"]=jwt.decode(request.headers['Authorization'][7:],SECRET_KEY, algorithms=['HS256'])['user_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = Review.objects.all().prefetch_related('userID')
        serializer = ReviewSerializerList(queryset, many=True)
        return Response(serializer.data)

class ReservationViewSet(BaseModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes=[IsAdminUser,]
    permission_action_classes = {
                'create': [IsAuthenticated],
    }

    def list(self, request, *args, **kwargs):
        queryset = Reservation.objects.all().prefetch_related()
        serializer = ReservationSerializerList(queryset, many=True)
        return Response(serializer.data)        

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user_reservations(request):
    queryset=Reservation.objects.filter(userID=jwt.decode(request.headers['Authorization'][7:],SECRET_KEY, algorithms=['HS256'])['user_id']).prefetch_related()
    serializer = ReservationSerializerList(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_reservation_dates(request,room):
    reservations=Reservation.objects.filter(roomID=room)
    serializer=ReservationSerializerBooked(reservations,many=True)
    return Response(serializer.data)

