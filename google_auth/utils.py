from google.auth.transport import requests
from google.oauth2 import id_token
from account.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from account.views import get_tokens_for_user
class Google():
    @staticmethod
    def validate(access_token):
        try:
            id_info=id_token.verify_oauth2_token(access_token,requests.Request())
            if "accounts.google.com" in id_info['iss']:
                return id_info
        except Exception as e:
            return "token is invalid or has expired"

def register_social_user(provider,email,first_name,last_name):
    user=User.objects.filter(email=email)
    if user.exists():
        if provider==user[0].auth_provider:
            login_user=authenticate(email=email,password=settings.SOCIAL_AUTH_PASSWORD)
            token=get_tokens_for_user(user)
            return {
                "user":login_user,
                "token":token
                        
            }
        else:
            raise AuthenticationFailed(
                detail=f"please continue your login with {user[0].auth_provider}"
                )
    new_user={
            'email':email,
            "first_name":first_name,
            "last_name":last_name,
            "password":settings.SOCIAL_AUTH_PASSWORD
        }

    register_user=User.objects.create_user(**new_user)
    register_user.auth_provider=provider 
    register_user.save()
    login_user=authenticate(email=email,password=settings.SOCIAL_AUTH_PASSWORD)
    token=get_tokens_for_user(user)
    return {
            "user":login_user,
            "token":token
                    
            } 


