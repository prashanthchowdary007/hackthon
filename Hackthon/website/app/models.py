from django.db import models


# Create your models here.
class bathroom(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    days = models.IntegerField()
    image = models.ImageField(upload_to='imgbathroom/')


class bedroom(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    days = models.IntegerField()
    image = models.ImageField(upload_to='imgbedroom/')


class kitchen(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    days = models.IntegerField()
    image = models.ImageField(upload_to='imgkitchen/')


class wardrobe(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    days = models.IntegerField()
    image = models.ImageField(upload_to='imgwardrobe/')


class livingroom(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    days = models.IntegerField()
    image = models.ImageField(upload_to='imglivingroom/')

