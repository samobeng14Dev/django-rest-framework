from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'


class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """ 
        a view for creating and listing posts

    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    queryset = Post.objects.all()

    @swagger_auto_schema(
            operation_summary="List of posts",
            operation_description="Returns a list of all posts",
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_summary="Create a post",  
            operation_description="Creates a new post",)
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
        a view for retrieving, updating and deleting posts
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]
    
    @swagger_auto_schema(
            operation_summary="Retrieve a post",
            operation_description="Returns a single post",
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_summary="Update a post",
            operation_description="Updates a post",
    )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_summary="Delete a post",
            operation_description="Deletes a post",
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    """
        a view for listing posts for a specific author
    """


class ListPostsForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username') or None

        if username is not None:
            return Post.objects.filter(author__username=username)
        else:
            return super().get_queryset()
        
    @swagger_auto_schema(
            operation_summary="List of posts for a specific author",
            operation_description="Returns a list of all posts for a specific author",
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self,request:Request, *args, **kwargs):
    #     post=Post.objects.all()
    #     serializer=self.serializer_class(instance=post, many=True)
    #     response={"message":"List of posts", "data":serializer.data}
    #     return Response(data=response, status=status.HTTP_200_OK)

    # def post(self,request:Request, *args, **kwargs):
    #     data=request.data
    #     serializer=self.serializer_class(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         response={"message":"Post created", "data":serializer.data}
    #         return Response(data=response, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request:Request, post_id:int, *args, **kwargs):
    #     post=get_object_or_404(Post, pk=post_id)
    #     serializer=self.serializer_class(instance=post)
    #     response={"message":"Post retrieved", "data":serializer.data}
    #     return Response(data=response, status=status.HTTP_200_OK)

    # def put(self,request:Request, post_id:int, *args, **kwargs):
    #     post=get_object_or_404(Post, pk=post_id)
    #     data=request.data
    #     serializer=self.serializer_class(instance=post, data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         response={"message":"Post updated", "data":serializer.data}
    #         return Response(data=response, status=status.HTTP_200_OK)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request:Request, post_id:int, *args, **kwargs):
    #     post=get_object_or_404(Post, pk=post_id)
    #     post.delete()
    #     response={"message":"Post deleted"}
    #     return Response(data=response, status=status.HTTP_204_NO_CONTENT)
