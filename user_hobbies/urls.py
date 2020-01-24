from django.urls import path, include
from .views import UserViewSet
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user_view')
router.register('hobbies', views.HobbiesViewSet, basename='hobbies')
router.register('rating', views.RatingViewSet, basename='rating')
router.register('profile', views.ProfileViewSet, basename='profile'),
router.register('hobby', views.SetHobbiesViewSet, basename='hobby'),
router.register('department', views.SetDepartmentViewSet, basename='department')

urlpatterns = [
]
urlpatterns += router.urls

