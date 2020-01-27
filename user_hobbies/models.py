from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()
# Create your models here.

profile_status = (
    ("1", "is_active"),
    ("2", "deactivated")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    status = models.CharField(max_length=20, choices=profile_status, default="1")
    is_delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Hobbies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserHobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    # hobby = models.ForeignKey(Hobbies, on_delete=models.CASCADE, related_name="User_Hobby")
    hobby = models.ManyToManyField(Hobbies)
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


class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserDepartments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username