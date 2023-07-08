from enum import unique
from pickle import TRUE
from tkinter.tix import Tree
from django.db import models

class customer(models.Model):
   fname=models.CharField(max_length=100)
   lname=models.CharField(max_length=100)
   address=models.TextField()
   pincode=models.IntegerField()
   mobile=models.CharField(max_length=10)
   username=models.CharField(max_length=100,unique=True)
   email=models.EmailField(max_length=254,unique=True)
   password1=models.CharField(max_length=30)



class seller(models.Model):
   name=models.CharField(max_length=100)
   address=models.TextField()
   mobile=models.CharField(max_length=10)
   username=models.CharField(max_length=100,unique=True)
   email=models.EmailField(max_length=254,unique=True)
   password1=models.CharField(max_length=30)


class product(models.Model):
   name=models.CharField(max_length=100)
   type=models.CharField(max_length=100)
   description=models.TextField()
   cost=models.IntegerField()
   quantity=models.IntegerField()
   sellerid=models.ForeignKey(seller,on_delete=models.CASCADE)


class soldproduct(models.Model):
   class Meta:
      unique_together = (('pid','cid'))
   pid=models.ForeignKey(product,on_delete=models.SET_NULL,null=TRUE)
   cid=models.ForeignKey(customer,on_delete=models.CASCADE,null=TRUE)
   quantitywished=models.IntegerField()
   cost=models.IntegerField()

   
