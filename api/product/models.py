from django.db import models
from api.category.models import Category

# Create your models here.
class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
