from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewset, CommentViewset, CategoryViewset

router = DefaultRouter()
router.register('posts', PostViewset, basename="post")
router.register('comments', CommentViewset, basename="comment")
router.register('categories', CategoryViewset, basename="category")

urlpatterns = [
    path('api/', include(router.urls)),
    # path('blog/<int:pk>/related/', related_blogs_view, name='related-blogs'),
]
