from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User,Category,Personaldetail
from .serializers import UserSerializer,CategorySerializer,PersonaldetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class CustomUserPagination(PageNumberPagination):
    page_size = 1  # Har page pe 10 users show honge
    page_size_query_param = 'page_size'
    max_page_size = 50 
class userviewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    pagination_class = CustomUserPagination #pagination
    authentication_classes = [JWTAuthentication]
class CustomTokenView(TokenObtainPairView):

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "Please send a POST request with username & password to get a token."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

class CustomTokenRefreshView(TokenRefreshView):
    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "Please send a POST request with a valid refresh token."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
class categoryviewset(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class = CustomUserPagination #pagination
class personaldetailviewset(ModelViewSet):
    queryset=Personaldetail.objects.all()
    serializer_class=PersonaldetailSerializer
    pagination_class = CustomUserPagination #pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['text', 'category']
    search_fields = ['text']  # ✅ Searching enable karein
    ordering_fields = ['text']  # ✅ Ordering enable karein
    ordering = ['text'] 
#     🔹 Filter by text:
# http://127.0.0.1:8000/api/personaldetails/?text=some_value

# 🔹 Filter by category ID:
# http://127.0.0.1:8000/api/personaldetails/?category=1

# 🔹 Search in text field:
# http://127.0.0.1:8000/api/personaldetails/?search=keyword

# 🔹 Order by text (ascending):
# http://127.0.0.1:8000/api/personaldetails/?ordering=text

# 🔹 Order by text (descending):
# http://127.0.0.1:8000/api/personaldetails/?ordering=-text