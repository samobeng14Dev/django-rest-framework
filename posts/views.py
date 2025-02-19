from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404






class PostListCreateView(APIView):
    """ 
        a view for creating and listing posts

    """
    serializer_class = PostSerializer


    def get(self,request:Request, *args, **kwargs):
        post=Post.objects.all()
        serializer=self.serializer_class(instance=post, many=True)
        response={"message":"List of posts", "data":serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self,request:Request, *args, **kwargs):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response={"message":"Post created", "data":serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveUpdateDeleteView(APIView):
    """
        a view for retrieving, updating and deleting posts
    """
    serializer_class = PostSerializer

    def get(self,request:Request, post_id:int, *args, **kwargs):
        post=get_object_or_404(Post, pk=post_id)
        serializer=self.serializer_class(instance=post)
        response={"message":"Post retrieved", "data":serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self,request:Request, post_id:int, *args, **kwargs):
        post=get_object_or_404(Post, pk=post_id)
        data=request.data
        serializer=self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()
            response={"message":"Post updated", "data":serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request:Request, post_id:int, *args, **kwargs):
        post=get_object_or_404(Post, pk=post_id)
        post.delete()
        response={"message":"Post deleted"}
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)  
    



  