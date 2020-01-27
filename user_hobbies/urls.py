from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user_view')
router.register('hobbies', views.HobbiesViewSet, basename='hobbies')
router.register('rating', views.RatingViewSet, basename='rating')
router.register('profile', views.ProfileViewSet, basename='profile'),
router.register('hobby', views.SetHobbiesViewSet, basename='hobby'),
router.register('department', views.SetDepartmentViewSet, basename='department'),
router.register('login', views.LoginViewSet, basename='login'),
router.register('get_dept', views.GetDepartmentViewSet, basename='get_dept')

urlpatterns = [
]
urlpatterns += router.urls

