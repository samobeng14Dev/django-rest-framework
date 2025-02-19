from django.urls import path
from .views import  PostListCreateView, PostRetrieveUpdateDeleteView

urlpatterns = [
    # path('homepage/', homepage, name='homepage'),
    path('', PostListCreateView.as_view(), name='list_posts'),
    path('<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post_detail'),
    # path('update/<int:post_id>/', update_post, name='update_post'),
    # path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
