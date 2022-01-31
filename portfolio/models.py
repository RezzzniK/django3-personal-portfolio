from django.db import models

# Create your models here.
class Project(models.Model):#declaring class of our models
                            # & injecting django model class to use its functions
    title=models.CharField(max_length=100)          #to use apropriate setting
    description=models.CharField(max_length=250)     #for properties
    image=models.ImageField(upload_to='portfolio/images')#we using django model
    url=models.URLField(blank=True)                                          #fields documentation

    #ADDING FUNCTION TO CHANGE REPERESENTATION ON ADMIN PAGE
    def __str__(self):
        return self.title
