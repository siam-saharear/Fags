from django.db import models



class Rng(models.Model):
    array = models.CharField(max_length=1000)
    def __str__(self):
        return self.array


class Fags(models.Model):
    
    fag = models.CharField(max_length = 100,default='Cigarette')
    price = models.IntegerField(default=0)
    switch = models.BooleanField(default=False)
    def __str__(self):
        return self.fag   

class Found_in(models.Model):
    fags = models.ForeignKey(Fags, on_delete=models.CASCADE)
    city = models.CharField(max_length = 100)
    def __str__(self):
        return self.city