from django.db import models



class MenuHotter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='images')

class MenuSalads(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='images')

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images')
