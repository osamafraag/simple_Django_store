from django.db import models
from django.shortcuts import reverse
from categories.models import Category
from django.contrib.auth.models import  User

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="store/images/", blank=True, null=True)
    instock = models.BooleanField(default=True)
    description = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return f"{self.name}"
    
    def details_url (self):
        return reverse('product.details', args=[self.id])
    
    def delete_url (self):
        return reverse('product.delete', args=[self.id])
    
    def edit_url (self):
        return reverse('product.edit', args=[self.id])
    
    @classmethod
    def products(cls) :
        return cls.objects.all()
    
    @classmethod
    def get(cls,id) :
        return cls.objects.get(id=id)
    
    def image_url(self) :
        return f"/media/{self.image}"