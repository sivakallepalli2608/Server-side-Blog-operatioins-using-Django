from rest_framework import serializers 
from .models import User,Blog,Comment,CodeBlock

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name','password']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','author'] 


class CommentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = "__all__"

class CodeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = "__all__"
  