from rest_framework import serializers
from account.models import User

class UserRegistationSerialiazer(serializers.ModelSerializer):
    # we are write this becouse we need confirm password field in our registration Request 
    password2=serializers.CharField(style={'input_type':"password"},write_only=True) 
    class Meta:
        model=User
        fields=['email','first_name','last_name','organization','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    #  validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("Password and Confirm Pasword doesn't match")
        return attrs
    def create(self, validated_data):
        password2 = validated_data.pop('password2', None)
        return User.objects.create_user(**validated_data)


class UserLoginSerialiazer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email', 'password']





 
            
       

   
        
