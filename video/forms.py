from django import forms

class TextForm(forms.Form):
    text_value = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
         'class': "input",
         'class': "form-control",
         'placeholder': "Enter Text Here...",
         'style': 'width:500px',         
         })
    )
