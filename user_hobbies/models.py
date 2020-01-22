from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

profile_status = (
    ("1", "is_active"),
    ("2", "deactivated")
)

#
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField()
#     mobile = models.IntegerField()
#     about = models.TextField()
#
#     def __str__(self):
#         return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    status = models.CharField(max_length =20, choices =profile_status, default="1")
    is_delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Hobbies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserHobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_Hobby")
    hobby = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_givenby")
    honesty = models.IntegerField(default=0,
           validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
        ])
    hardwork = models.IntegerField(default=0,
           validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
        ])

