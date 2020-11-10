from django import forms
from .models import Assortment
class AssortmentForm(forms.ModelForm):
 class Meta:
  model = Assortment
  fields = ('Category', 'Type')
