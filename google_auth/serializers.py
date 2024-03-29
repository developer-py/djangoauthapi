from rest_framework import serializers
from .utils import Google, register_social_user
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

class GoogleSignSerializer(serializers.Serializer):
    access_token=serializers.CharField(min_length=6)

    def validate_access_token(self,access_token):
        try:
            google_user_data=Google.validate(access_token)
            user_id=google_user_data["sub"]

        except KeyError:
            raise serializers.ValidationError("This token is invalid or has been expired")
        except Exception as e:
            raise serializers.ValidationError(f"Error validating access token: {str(e)}")
        
        if google_user_data["aud"]!=settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed(detail="Could not verify user")
        email=google_user_data['email']
        first_name=google_user_data['given_name']
        last_name=google_user_data['family_name']
        provider="google"
        return register_social_user(provider,email,first_name,last_name)
    




      
            
            
     
           
      

        
           

    
      
    


