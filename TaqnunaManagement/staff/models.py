from django.db import models
from django.forms import CharField, ChoiceField

# Create your models here.



class Teams(models.Model):
    teamCategure = models.CharField(max_length=15)
    teamDescription = models.CharField(max_length=150,blank=True,null=True)
    def  __str__(self):
         return self.teamCategure
    
    

class Employee(models.Model):
      name = models.CharField(max_length=20,blank=True,null=True)
      teams = models.ForeignKey(Teams,on_delete=models.PROTECT,null=True,blank=True)
   
      def  __str__(self):
         return self.name
      
    
    
   