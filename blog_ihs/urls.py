from django.urls import path, include
from rest_framework import routers
from blog_ihs.views import ArticleViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]