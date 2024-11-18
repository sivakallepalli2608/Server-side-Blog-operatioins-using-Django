from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .tokengen import *
from .authentication import *
from level_3 import authentication


@api_view(['POST'])
def sign_up(request):
    user_name = request.data['user_name']
    password = request.data['password']
    serializer = UserSerializer(data = {'user_name':user_name,'password':password})
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'user created'},status=status.HTTP_201_CREATED)
    return Response({'message':'user_name already exists'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sign_in(request):
    user_name = request.data['user_name']
    password = request.data['password']
    user = User.objects.filter(user_name = user_name,password = password)
    if not user:
        return Response({'invalid username/password'})
    access_token,refresh_token = generate_jwt(user[0])

    return Response({'access_token':access_token,'refresh_token':refresh_token})

@api_view(['POST'])
def gen_access_token(request):
    refreshToken = request.data['refresh']
    if not refreshToken:
        return Response('refresh token needed')
    decodeToken = decode_token(refreshToken)
    if isinstance(decodeToken,dict):
        user_name = decodeToken['user_id']
        user = User.objects.filter(user_name = user_name)[0]
        if user:
            access_token,refresh_token = generate_jwt(user)
            return Response({'access_token':access_token,'refresh_token':refresh_token})

    return Response({'error':'Invalid refresh token'})


@authenticate
@api_view(['POST'])
def create_blog(request):
    data = request.data
    data['author'] = request.user_id
    serializer = BlogSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@authenticate
@api_view(['POST'])
def media(request,blog_id):
    blog = Blog.objects.filter(blog_id = blog_id)[0]
    if blog:
        if blog.author_id == request.user_id:
            files = request.FILES.getlist('media')
            for file in files:
                if file.size>10*1024*1024:
                    return Response("Media size should be less than 10Mb")
                Media(blog = blog,media=file.read()).save()
        return Response({"You cannot access this blog"},status = status.HTTP_400_BAD_REQUEST)
    return Response("Blog does'nt exist")

@authenticate
@api_view(['POST'])
def addCode(request,blog_id):
    blog = Blog.objects.filter(blog_id = blog_id)[0]
    if blog:
        if blog.author_id == request.user_id:
            code_data = {
                'blog':blog_id,
                'code':request.data['code']
            }
        add_code = CodeSerializer(data = code_data)
        if add_code.is_valid():
            add_code.save()
            return Response({"added_code":add_code.data})
    return Response({"The code is not added"})
    

@authenticate
@api_view(['POST'])
def addComment(request,blog_id):
    Comment_id = request.GET.get('comment_id',None)
    Comment = {
        "user":request.user_id,
        "comment":request.data['comment'],
        "blog":blog_id,
        "parent_comment":Comment_id
        }
    comment = CommentSerializer(data = comment)
    if comment.is_valid():
        comment.save()
        return Response({"Comment":comment.data})
    return Response("Connot Comment")

@authenticate
@api_view(['POST'])
def like(request,comment_id):
    comment = Comment.objects.filter(comment_id = comment_id)
    if comment[0]:
        if comment.like.filter(user_id = request.user_id).exists():
            comment.likes.remove(request.user_id)
            return Response("Unliked")
        comment.likes.add(request.user_id)
        return Response("Liked")
