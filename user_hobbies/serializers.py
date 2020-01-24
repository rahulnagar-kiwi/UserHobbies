from .models import Hobbies, UserHobby, Profile, Rating, User, Departments, UserDepartments
from rest_framework import serializers
from django.db.models import Avg
from .messages import ERROR_CODE, SUCCESS_CODE
from django.contrib.auth import get_user_model, authenticate



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError(ERROR_CODE['4008'])
        return value

    @staticmethod
    def validate_password(value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError(ERROR_CODE['4008'])
        return value

    def create(self, validated_data):
            password = validated_data.pop('password')
            validated_data.update({'email': validated_data['email'].lower()})
            instance = User.objects.create(**validated_data)
            instance.set_password(password)
            instance.save()
            return instance


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['name',]


class UserHobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserHobby
        fields = ['user', 'hobby','is_active']

    # def create(self, validated_data):
    #     user = User.objects.get(pk= validated_data["pk"])
    #     hobby_pk = validated_data["hobby_pk"]


class ProfieSerializer(serializers.ModelSerializer):
    hobby = serializers.SerializerMethodField("get_hobby")
    name = serializers.CharField(source="user.username")
    honesty = serializers.SerializerMethodField("avg_honesty")
    hardwork = serializers.SerializerMethodField("avg_hardwork")
    hobby1 = HobbiesSerializer(many=True, read_only=True)

    def get_hobby(self, obj):
        serializer= UserHobbySerializer(obj.user.User_Hobby.all(), many=True)
        return serializer.data

    def avg_honesty(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('honesty'))
        return rating_qs["honesty__avg"]

    def avg_hardwork(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('hardwork'))
        return rating_qs["hardwork__avg"]

    class Meta:
        model = Profile
        fields = ['user', 'name', 'status', 'is_delete', 'created', 'hobby', 'honesty', 'hardwork', 'hobby1']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'given_by', 'honesty', 'hardwork']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password')

        def validate_email(self, value):
            user = User.objects.filter(email=value.lower())
            if not user.exists():
                raise serializers.ValidationError(ERROR_CODE['4009'])
            return value

        def create(self, validated_data):
            email = validated_data("email")
            password = validated_data("password")
            user = authenticate(email=email.lower(), password=password)
            if user:
                return user
            return User.objects.none


class UserDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDepartments
        fields = ('user', 'department')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('user',)