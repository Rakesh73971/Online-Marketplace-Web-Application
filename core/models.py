from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class NewItem(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='newitem')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    

    
