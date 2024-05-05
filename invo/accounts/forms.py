from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm): 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input100','placeholder':'Email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Company Name'}))
    #last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'input100'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'input100'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'input100', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'username', 
            'placeholder':'username', 
            }) 
        self.fields['password'].widget.attrs.update({ 
            'class': 'input100', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        
    class Meta:
        model = User
        fields = ('username', 'password')

