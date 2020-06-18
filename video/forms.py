from django import forms

class TextForm(forms.Form):
    text_value = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
         'class': "input",
         'class': 'form-control',
         'style': 'width: 600px',
         'placeholder': "enter words here to find ASL videos...",
         'style': 'align:center',
         'autocomplete': 'off',
         'style': 'margin-top:15px',
         })
    )
