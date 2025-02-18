from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer




@api_view(http_method_names=['GET', 'POST'])
def homepage(request: Request):
    if request.method == 'POST':
        data = request.data
        response = {"message": "Hello, World!", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello, World!"}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET', 'POST'])
def list_posts(request: Request):
    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "Post created", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    response = {"message": "posts", "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def post_detail(request:Request, post_index:int):
    post = posts[post_id]

    if post:
        return Response(data=post, status=status.HTTP_200_OK) 

    return Response(data={"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)     
  