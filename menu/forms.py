from django import forms
from .models import Task


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "judul",
            "deskripsi",
            "tanggal_jatuh_tempo",
            "kategori",
        ]
