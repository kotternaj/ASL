from django import forms

class TextForm(forms.Form):
    text_value = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
         'class': "input",
         'class': 'form-control',
         'style': 'width: 460px',
         'placeholder': "Enter Text Here...",
         'style': 'align:center',
         'autocomplete': 'off',
         'style': 'margin-bottom:10px',
         })
    )
