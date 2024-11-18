from rest_framework.response import Response
from .tokengen import *
from functools import wraps

def authenticate(view_func):
    @wraps(view_func)
    def wrapper(request,*args,**kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            print(token)
            decoded_token = decode_token(token)
            print(decoded_token)
            if decoded_token !=-1:
                request.user_id = decoded_token['user_id']
                return view_func(request,*args,**kwargs)
        return Response("You are not allowed")
    return wrapper
