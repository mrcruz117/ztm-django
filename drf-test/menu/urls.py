from django.urls import path

from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

router.register('items', views.ItemViewSet, basename='items')
router.register('users', views.UserViewSet, basename='users')
router.register('source_location', views.Source_locationViewSet, basename='source_location')

# urlpatterns = [
#     path('', views.item_list),
#     path('<int:pk>/', views.item_detail),

# ]

urlpatterns = router.urls
