from django import forms
class StudForm(forms.Form):
    Name = forms.CharField(label="Enter the name",max_length=20)

