from django.urls import path
from .views import homepage, list_posts, post_detail, update_post, delete_post

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('', list_posts, name='list_posts'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('update/<int:post_id>/', update_post, name='update_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
