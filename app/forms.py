from django.forms import ModelForm
from app.models import Pokemon

# Create the form class.
class PokemonForm(ModelForm):
     class Meta:
         model = Pokemon
         fields = ['name', 'typeOne', 'typeTwo', 'hp', 'attack', 'defense', 'spAttack', 'spDefense', 'speed']
