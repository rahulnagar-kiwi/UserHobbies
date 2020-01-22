from .models import Hobbies, UserHobby, Profile, Rating, User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # def update(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(data= request.data)
    #
    #     if serializer.is_valid():
    #         self.object.set_password(serializer.data.get("new_password"))
    #         self.object.save()


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['name',]


class UserHobbyySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserHobby
        fields = ['hobby', 'is_active']


class ProfieSerializer(serializers.ModelSerializer):
    hobby = serializers.SerializerMethodField("get_hobby")
    name = serializers.CharField(source="user.username")
    honesty = serializers.SerializerMethodField("avg_honesty")
    hardwork = serializers.SerializerMethodField("avg_hardwork")

    def get_hobby(self, obj):
        serializer= UserHobbyySerializer(obj.user.User_Hobby.all(), many=True)
        return serializer.data

    def avg_honesty(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('honesty'))
        return rating_qs["honesty__avg"]

    def avg_hardwork(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('hardwork'))
        return rating_qs["hardwork__avg"]

    class Meta:
        model = Profile
        fields = ['user', 'name', 'status', 'is_delete', 'created', 'hobby', 'honesty', "hardwork"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'given_by', 'honesty', 'hardwork']