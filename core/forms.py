from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username','email','password','confirmPassword'
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')

        if password and confirmPassword:
            if password != confirmPassword:
                raise forms.ValidationError("The passwords does not match")

        return super(UserRegisterForm, self).clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("The user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError('The username or password in incorrect')
            if not user.is_active:
                raise forms.ValidationError("The user is not active")

        return super(UserLoginForm, self).clean(*args, **kwargs)