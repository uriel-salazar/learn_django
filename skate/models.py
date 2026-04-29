from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    first_name = None
    last_name = None
    username=models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.username

class Spots(models.Model):
    name_spot = models.CharField(max_length = 30)
    body = models.TextField( null= True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_spot
    
class Rating(models.Model):
    score = models.DecimalField(max_digits=4,decimal_places=2)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spots, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = ('user', 'spot')

    def __str__(self):
        return f"{self.user} rated {self.spot} - {self.score}"
    