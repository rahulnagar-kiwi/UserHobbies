from django.contrib import admin
from .models import Profile, Hobbies, UserHobby, Rating
# Register your models here.

# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Hobbies)
admin.site.register(UserHobby)
admin.site.register(Rating)

