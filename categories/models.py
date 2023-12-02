from django.db import models

from django.shortcuts import reverse

class Category(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/images/", blank=True, null=True)
    description = models.CharField(max_length=300, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def details_url (self):
        return reverse('category.details', args=[self.id])
    
    def delete_url (self):
        return reverse('category.delete', args=[self.id])
    
    def edit_url (self):
        return reverse('category.edit', args=[self.id])
    
    @classmethod
    def categories(cls) :
        return cls.objects.all()
    
    @classmethod
    def get(cls,id) :
        return cls.objects.get(id=id)
    
    def image_url(self) :
        return f"/media/{self.image}"
