from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=122,default="No task")
     
    date= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    

        
    