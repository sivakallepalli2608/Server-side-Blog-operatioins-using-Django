from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length = 12)
    password = models.CharField(max_length = 12)
    id_num = models.AutoField(primary_key = True)

    def __str__(self):
        return self.user_name
    
class CodeBlock(models.Model):
    id = models.AutoField(primary_key = True)
    code = models.TextField()
    
class Blog(models.Model):
    blog_id = models.AutoField(primary_key = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    title = models.TextField()
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,blank=True,default=None)
    code = models.ManyToManyField(CodeBlock,blank = True,default = None)



class Media(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    media = models.BinaryField()

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="us")
    title = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,blank=True,default=None)



class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=15)

