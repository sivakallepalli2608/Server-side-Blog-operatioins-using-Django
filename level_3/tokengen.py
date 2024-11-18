import jwt 
import datetime
from django.conf import settings
from .models import User

def generate_jwt(user):
    access = {
        'user_id':User.objects.filter(user_name = user.user_name)[0].id_num,
        'exp':datetime.datetime.now(tz = datetime.timezone.utc)+datetime.timedelta(minutes=15)

    }

    refresh = {
        'user_id':User.objects.filter(user_name = user.user_name)[0].id_num,
        'exp':datetime.datetime.now(tz = datetime.timezone.utc)+datetime.timedelta(days = 1)
    }

    return jwt.encode(access,settings.SECRET_KEY[15:],algorithm = 'HS256'),jwt.encode(refresh,settings.SECRET_KEY)

def decode_token(token):
    try:
        return jwt.decode(token,settings.SECRET_KEY[15:],algorithms=['HS256'])
    except Exception as e:
        return -1