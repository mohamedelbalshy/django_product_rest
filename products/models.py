from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    creator = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering=['-id']
