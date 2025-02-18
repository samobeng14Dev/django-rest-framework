from django.urls import path
from .views import homepage, list_posts, post_detail  

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('', list_posts, name='list_posts'),
    path('<int:post_index>/', post_detail, name='post_detail'),
]
