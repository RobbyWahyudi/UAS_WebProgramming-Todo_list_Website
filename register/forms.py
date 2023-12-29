# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(help_text="Required. Format: YYYY-MM-DD")
    profile_picture = forms.ImageField(required=False)
    id_username = forms.TextInput(attrs={"class": "form-control"})

    # class Meta(UserCreationForm.Meta):
    #     model = UserCreationForm
    #     fields = [
    #         "username",
    #     ]

    #     widgets = {"username": forms.TextInput(attrs={"class": "form-control"})}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Tambahkan class Bootstrap di sini
    #     for field_name in self.fields:
    #         self.fields[field_name].widget.attrs["class"] = "form-control"
