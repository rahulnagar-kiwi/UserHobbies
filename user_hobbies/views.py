
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import (UserHobby, Profile, Rating, UserDepartments)
from .serializers import (UserHobbySerializer, ProfieSerializer, RatingSerializer, UserSerializer, LoginSerializer,
                          UserDepartmentSerializer, GetDepartmentSerializer)


# Create your views here.


class UserViewSet(GenericViewSet):
    @action(methods=['post'], url_name='signup', url_path='signup', serializer_class=UserSerializer, detail=False)
    def signup(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginViewSet(GenericViewSet):
    @action(methods=['post'], url_name='login', url_path='login', serializer_class=LoginSerializer, detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if not user:
           return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)


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


# class SetDepartmentViewSet(GenericViewSet):
#     @action(methods=['POST'], url_name="setdepartment", url_path="setdepartment",
#             serializer_class=UserDepartmentSerializer,
#             detail=False)
#     def set_hobby(self, request):
#         user_obj = User.objects.get(pk=request.data["user_id"])
#         for i in request.data["department_list"]:
#             department_obj = Departments.objects.get(pk=i)
#             user_hobby_qs = UserDepartments(user=user_obj, department=department_obj)
#             dept_serializer = UserDepartmentSerializer(user_hobby_qs)
#             serializer = UserDepartmentSerializer(data=dept_serializer.data)
#             if serializer.is_valid():
#                 serializer.save()
#         return Response({'hobbies': serializer.data})


class GetDepartmentViewSet(GenericViewSet):

    @action(methods=['GET'], url_name="get_department", url_path="get_department",
            serializer_class=GetDepartmentSerializer, detail=False)
    def get_hobby(self, request):
        departments_qs = UserDepartments.objects.all()
        serializer = GetDepartmentSerializer(departments_qs, many=True)
        return Response({'departments': serializer.data})


class SetDepartmentViewSet(GenericViewSet):
    @action(methods=['POST'], url_name="setdepartment", url_path="setdepartment",
            serializer_class=UserDepartmentSerializer,
            detail=False)
    def set_hobby(self, request):
        serializer = UserDepartmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# class SetDepartmentViewSet(GenericViewSet):
#     @action(methods=['POST'], url_name="setdepartment", url_path="setdepartment",
#             serializer_class=UserDepartmentSerializer,
#             detail=False)
#     def set_hobby(self, request):
#         user_id = request.data['user_id']
#         department_list = request.data['department_list']
#         serializer = self.serializer_class({'user_id': user_id, 'department_list': department_list}, partial=True)
#         serializer_instance = UserDepartmentSerializer(data=serializer.data)
#         if serializer_instance.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
