from django.db import models

class User(models.Model):
    
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

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
    