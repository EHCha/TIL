from django import forms
from .models import Todos

class TodosForm(forms.ModelForm):

    class Meta:
        model = Todos
        # fields = '__all__'
        exclude = ('user',)