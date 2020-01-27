from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import serializers

from .messages import ERROR_CODE
from .models import Hobbies, UserHobby, Profile, Rating, User, Departments, UserDepartments

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    sumit = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = User
        fields = ['password', 'email', "sumit"]

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

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
            password = validated_data.pop('password')
            validated_data.update({'email': validated_data['email'].lower()})
            instance = User.objects.create(email=validated_data['email'].lower())
            instance.set_password(password)
            instance.save()
            return instance


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['name',]


class UserHobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserHobby
        fields = ['hobby',]


class ProfieSerializer(serializers.ModelSerializer):
    hobby_list = serializers.SerializerMethodField("get_hobby")
    name = serializers.CharField(source="user.username")
    honesty = serializers.SerializerMethodField("avg_honesty")
    hardwork = serializers.SerializerMethodField("avg_hardwork")

    def get_hobby(self, obj):
         return obj.user.User.values_list('hobby__name', 'hobby__id').all()

    def avg_honesty(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('honesty'))
        return rating_qs["honesty__avg"]

    def avg_hardwork(self, obj):
        rating_qs = obj.user.user_rating.all().aggregate(Avg('hardwork'))
        return rating_qs["hardwork__avg"]

    class Meta:
        model = Profile
        fields = ['user', 'name', 'status', 'is_delete', 'created', 'hobby_list', 'honesty', 'hardwork']


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
            email = validated_data["email"]
            password = validated_data["password"]
            user = User.objects.filter(email=email.lower())
            if user.exists():
                user = user.first()
                if user.check_password(password):
                   return user
                return User.objects.none()
            return User.objects.none()


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('name',)


class UserDepartmentSerializer(serializers.ModelSerializer):
    department = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all()))

    class Meta:
        model = UserDepartments
        fields = ('user', 'department')


class GetDepartmentSerializer(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField('get_name')
    username = serializers.SerializerMethodField("get_user")

    def get_name(self, obj):
        return obj.department.name

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = UserDepartments
        fields = ('dept_name', 'user','username')
