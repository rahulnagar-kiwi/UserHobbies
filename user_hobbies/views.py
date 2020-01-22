from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Hobbies, UserHobby, Profile, Rating, User
from .serializers import UserHobbyySerializer, HobbiesSerializer, ProfieSerializer,\
                      RatingSerializer, UserSerializer
from rest_framework import viewsets, status, mixins


# Create your views here.


def check(request):
    return HttpResponse("we are here")


class UserViewSet(GenericViewSet):
    @action(methods=['post'], url_name='signup', url_path='signup', serializer_class=UserSerializer, detail=False)
    def signup(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_name='login', url_path='login', serializer_class=UserSerializer, detail=False)
    def login(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password = password)
        if user is not None:
            login(request, user)
            return HttpResponse("in")
        return HttpResponse("not in")


class HobbiesViewSet(GenericViewSet, mixins.ListModelMixin):

    @action(methods=["GET"], url_name="hobby_list", url_path="hobby_list", serializer_class=UserHobbyySerializer,
            detail=False)
    def get_hobby(self, request):
        hobby_qs = UserHobby.objects.all()
        serializer = UserHobbyySerializer(hobby_qs, many=True)
        return Response({'hobbies': serializer.data})


# class RatingViewSet(GenericViewSet, mixins.ListModelMixin):
#
#     @action(methods=["POST"], url_name="post_rating", url_path="post_rating", serializer_class=RatingSerializer,
#             detail=False)
#     def post_rating(self, request):
#
#         rating_qs = Rating.objects.all()
#         serializer = UserHobbyySerializer(rating_qs, many=True)
#         return Response({'hobbies': serializer.data})


class RatingViewSet(viewsets.ModelViewSet):
    model = Rating
    serializer_class = RatingSerializer


class ProfileViewSet(GenericViewSet):

    @action(methods=['GET'], url_name='user', url_path='user', serializer_class=ProfieSerializer, detail=False)
    def get_prfile(self, request):
        profile_qs = Profile.objects.all()
        serializer = ProfieSerializer(profile_qs, many=True)
        return Response({'user': serializer.data})
