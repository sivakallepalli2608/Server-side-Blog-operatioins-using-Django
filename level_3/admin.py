from django.contrib import admin
from .models import User,Blog,Comment,CodeBlock
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(CodeBlock)