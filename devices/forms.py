from django import forms

from .models import User as user
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    #users = forms.ModelChoiceField(User.objects.all())


    class Meta:
        model = User
        fields = ('username','password')
        labels = {'username': 'Usuário',}

    def clean(self):
        cleaned_data = super().clean()
        username1 = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password')

        if username1 == password1:
            raise forms.ValidationError('deu ruim')

        return cleaned_data

