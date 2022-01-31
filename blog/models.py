from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    text=models.TextField()
    #ADDING FUNCTION TO CHANGE REPERESENTATION ON ADMIN PAGE
    def __str__(self):
        return self.title
