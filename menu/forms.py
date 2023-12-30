from django import forms
from .models import Task


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "judul",
            "tanggal_jatuh_tempo",
            "kategori",
        ]

        widgets = {
            "judul": forms.TextInput(attrs={"class": "form-control"}),
            "tanggal_jatuh_tempo": forms.TextInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "kategori": forms.Select(attrs={"class": "form-control"}),
        }
