from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('posts/<int:post_id>/', views.PostDetail.as_view(), name='post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
