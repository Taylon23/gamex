from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Username"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Senha"
    }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Nome ou senha incorreto(s)')

            return user


class UserResisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "name@gmail.com"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Senha"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Senha"
    }))

    def clean():
        cleaned_data = super().clean()
        username = cleaned_data['username']
        email = cleaned_data['email']
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('As senhas não coincidem')
        
        if len(username) < 4:
            raise forms.ValidationError('Username deve conter minimo 4 caracteres ')
        
        if len(password1) < 8:
            raise forms.ValidationError('A senha deve conter minimo 8 caracteres ')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('O email ja esta em uso')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username ja esta em uso')
        
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self,commit=True):
        user = super(UserResisterForm,self).save(commit=True)

        user.email= self.cleaned_data.get('email')

        if commit:
            user.save()
        
        return user
