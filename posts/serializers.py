from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # validation
    title = serializers.CharField(max_length=50)
   
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created']



# The PostSerializer class is a subclass of the ModelSerializer class from the rest_framework module. The ModelSerializer class provides a way to serialize and deserialize model instances into representations such as JSON. The PostSerializer class specifies the model and fields to be serialized. In this case, it specifies the Post model and the id, title, content, and created fields to be included in the serialized representation of a Post instance.