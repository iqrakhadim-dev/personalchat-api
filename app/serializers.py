from rest_framework import serializers
from .models import User, Category,Personaldetail
# from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
       

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PersonaldetailSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    user= serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Personaldetail
        fields = '__all__'
