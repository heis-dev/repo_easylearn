from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','is_platform_admin']
        extra_kwargs = {'password':{'write_only': True}}