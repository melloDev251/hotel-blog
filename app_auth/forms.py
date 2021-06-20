from django import forms

class LoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:0rem'}))
    pwd = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'margin-bottom:0rem'}))

class RegisterForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:0rem'}))
    pwd = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'margin-bottom:0rem'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'style':'margin-bottom:0rem'}))