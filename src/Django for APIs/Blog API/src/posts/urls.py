from .views import PostList, PostDetail
from django.urls import path

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list")

]
