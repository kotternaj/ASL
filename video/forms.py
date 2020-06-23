from django import forms

class TextForm(forms.Form):
    text_value = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
         'class': 'input',
         'class': 'form-control',
         'placeholder': "Search for ASL Videos",
         'style': 'align:center',
         'autocomplete': 'off',
         'style': 'margin-top: 15px',
         # 'style': 'background-color:#121212',
         })
    )
