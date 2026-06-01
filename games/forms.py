from django import forms
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# =========================
# GAME FORM
# =========================

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'description',
            'category',
            'price',
            'original_price',
            'discount_percent',
            'image',
        ]
# =========================
# REGISTER FORM
# =========================

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        ]