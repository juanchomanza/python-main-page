from django.db import models

# Create your models here.




class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    career = models.CharField(max_length=100)
    

    def __str__(self):
        return f'Persona {self.id}: {self.name} {self.surname} email: {self.email}'

    



class ChampFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    champ = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    runes = models.CharField(max_length=100)
    explication = models.TextField()


class Agent(models.Model):
    agent = models.CharField(max_length=255, primary_key=True)
    type_choices = (('Controller', 'Controller'),('Duelist', 'Duelist'),('Sentinel','Sentinel'),('Initiator','Initiator'))
    gender_choices = (('Man', 'Man'),('Woman','Woman'))
    type = models.CharField(max_length=255, choices=type_choices)
    gender = models.CharField(max_length=255, choices=gender_choices)
    photo = models.ImageField(upload_to='agents', null=True)
    




   
    
