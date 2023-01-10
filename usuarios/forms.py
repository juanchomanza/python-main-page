from django.forms import ModelForm, EmailInput
from django import forms
from usuarios.models import Agent, User, ChampFav

class PersonaNueva(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets ={
            'email': EmailInput(attrs={'type':'email'})


        }




class Champ(ModelForm):
    class Meta:
        model = ChampFav
        fields = '__all__'
        widgets = {


        }


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            
        }
    

class Calculadora(forms.Form):
    number_1 = forms.IntegerField()
    number_2 = forms.IntegerField()