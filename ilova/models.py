from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 200)
    definition1 = models.TextField(blank = True)
    definition2 = models.TextField(blank = True)
    definition3 = models.TextField(blank = True)
    definition4 = models.TextField(blank = True)
    definition5 = models.TextField(blank = True)
    image = models.ImageField(blank = True)


class Call(models.Model):
    qayerdan = models.CharField(max_length = 300)
    phone = models.IntegerField()
    content = models.TextField(blank = True)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)

class Portfolio(models.Model):
    is_landing = models.CharField(max_length = 300)
    image = models.ImageField()
    image_desktop = models.ImageField
    image_phone_name = models.ImageField()
    description = models.CharField(max_length = 300)
    category = models.CharField(max_length=300)

class Massage(models.Model):
    name = models.CharField(max_length = 300)
    phone = models.IntegerField()
    email = models.CharField(max_length = 300)
    content = models.TextField(blank = True)

class Otziv(models.Model):
    name = models.CharField(max_length = 300)
    link = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)


class News(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    image = models.ImageField(blank = True)

    
    

# Create your models here.
