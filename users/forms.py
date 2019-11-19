from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Carnes

class CarnesForm(forms.ModelForm):

    class Meta:
        model = Carnes
        fields = (
            'tipo', 
            'titulo',
            'marca',
            'precio_kilo',
            'peso',
            'precio_total',
            )

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'tipo')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'tipo')