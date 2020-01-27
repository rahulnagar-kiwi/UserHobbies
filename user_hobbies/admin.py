from django.contrib import admin

from .models import Profile, Hobbies, UserHobby, Rating, Departments, UserDepartments

# Register your models here.

admin.site.register(Departments)
admin.site.register(UserDepartments)
admin.site.register(Profile)
admin.site.register(Hobbies)
admin.site.register(UserHobby)
admin.site.register(Rating)

