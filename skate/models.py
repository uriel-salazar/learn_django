from django.db import models

class User(models.Model):
    
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Spots(models.Model):
    name_spot = models.CharField(max_length = 30,null = False)
    body = models.TextField(max_length = 200, null= True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_spot
    