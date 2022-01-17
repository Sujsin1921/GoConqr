from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=100)  
    level = models.CharField(max_length=100)
    technology = models.CharField(max_length=100) 
    description = models.CharField(max_length=450)
    doc_link = models.CharField(max_length=150)
    link = models.CharField(max_length=500)
    followup = models.CharField(max_length=120)  

    def __str__(self):
        return self.title

class userprofill(models.Model):
    name = models.CharField(max_length=60)
    email =models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    background = models.CharField(max_length=20) 
    category = models.CharField(max_length=80)
    language = models.CharField(max_length=60)
    front = models.CharField(max_length=100)
    level = models.CharField(max_length=45)
    technology = models.CharField(max_length=70)
    

    def __str__(self):
        return self.category

