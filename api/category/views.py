from rest_framework import viewsets
from .serializers import CategorySerializer
from rest_framework.response import Response
from .models import Category


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("name")
