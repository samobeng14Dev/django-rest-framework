from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView, ListPostsForAuthor

urlpatterns = [
    # path('homepage/', homepage, name='homepage'),
    path('', PostListCreateView.as_view(), name='list_posts'),
    path('<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post_detail'),
    path('posts_for_author/<str:username>/',
         ListPostsForAuthor.as_view(), name='posts_for_author'),
    # path('update/<int:post_id>/', update_post, name='update_post'),
    # path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
