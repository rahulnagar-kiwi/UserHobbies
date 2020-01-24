from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .messages import ERROR_CODE, SUCCESS_CODE
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Hobbies, UserHobby, Profile, Rating, User ,UserDepartments, Departments
from .serializers import UserHobbySerializer, HobbiesSerializer, ProfieSerializer,\
                      RatingSerializer, UserSerializer, LoginSerializer, UserDepartmentSerializer
from rest_framework import viewsets, status, mixins
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


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

    @action(methods=['post'], url_name='login', url_path='login', serializer_class=LoginSerializer, detail=False)
    def login(self, request):
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if not user:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        # if not user.is_email_verified:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    @action(methods=['post'], url_name='logout', url_path='logout' , detail=False)
    def logout(self, request):
        request.user.logout(access_token=request.META['HTTP_AUTHORIZATION'].split(" ")[1])
        return Response({'detail': SUCCESS_CODE['2001']})


class HobbiesViewSet(GenericViewSet, mixins.ListModelMixin):

    @action(methods=["GET"], url_name="hobby_list", url_path="hobby_list", serializer_class=UserHobbySerializer,
            detail=False)
    def get_hobby(self, request):
        hobby_qs = UserHobby.objects.all()
        serializer = UserHobbySerializer(hobby_qs, many=True)
        return Response({'hobbies': serializer.data})


class RatingViewSet(viewsets.ModelViewSet):
    model = Rating
    serializer_class = RatingSerializer


class ProfileViewSet(GenericViewSet):

    @action(methods=['GET'], url_name='user', url_path='user', serializer_class=ProfieSerializer, detail=False)
    def get_pofile(self, request):
        profile_qs = Profile.objects.all()
        serializer = ProfieSerializer(profile_qs, many=True)
        return Response({'user': serializer.data})


class SetHobbiesViewSet(GenericViewSet):
    @action(methods=['POST'], url_name="sethobby", url_path="sethobby", serializer_class=UserHobbySerializer,
            detail=False)
    def set_hobby(self, request):
        profile_qs = UserHobby.objects.get(pk=request.data["user_id"])
        for i in request.data["hobby_list"]:
            profile_qs.hobby.add(i)
        serializer = UserHobbySerializer(profile_qs)
        return Response({'hobbies': serializer.data})


class SetDepartmentViewSet(GenericViewSet):
    @action(methods=['POST'], url_name="setdepartment", url_path="setdepartment", serializer_class=UserDepartmentSerializer,
            detail=False)
    def set_hobby(self, request):
        user_obj = User.objects.get(pk=request.data["user_id"])
        for i in request.data["department_list"]:
            department_obj = Departments.objects.get(pk=i)
            user_hobby_qs = UserDepartments(user=user_obj, department=department_obj)
            serializer = UserDepartmentSerializer(user_hobby_qs)
            if serializer.is_valid():
                 serializer.save()
        return Response({'hobbies': serializer.data})

    # @action(methods=['GET'], url_name="gethobby", url_path="gethobby", serializer_class=UserHobbySerializer, detail=False)
    # def set_hobby(self, request):
    #         profile_qs = UserHobby.objects.all()
    #         serializer = UserHobbySerializer(profile_qs, many=True)
    #         return Response({'hobbies': serializer.data})


        # check_qs = UserHobby.objects.get(pk=request.data["user_id"])
        # if check_qs:
        #     UserHobby.objects.get(pk=request.data["user_id"]).delete()
        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # profile_qs = UserHobby(user=User.objects.get(pk=request.data["user_id"]))
        # profile_qs.save()
        # for i in request.data["hobby_list"]:
        #     profile_qs.hobby.add(i)
        # serializer = UserHobbySerializer(profile_qs)
        # return Response({'hobbies': serializer.data})
