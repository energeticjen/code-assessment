from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "title", "age", "hometown"]

    name = forms.CharField(label="Name", required=True)
    title = forms.CharField(label="Title", required=True)
    age = forms.IntegerField(label="Age", required=False)
    hometown = forms.CharField(label="Hometown", required=False)


