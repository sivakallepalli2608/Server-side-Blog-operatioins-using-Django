from django.urls import path
from . import views
urlpatterns = [
    path('addcode/<int:blog_id>',views.addCode),
    path('addcomment/<int:blog_id>',views.addComment),
    path('signup/',views.sign_up),
    path('signin/',views.sign_in),
    path('likecomment/<int:comment_id>',views.like),
    path('addmedia/<int:blog_id>',views.media),
    path('createblog/',views.create_blog)
]