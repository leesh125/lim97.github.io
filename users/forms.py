from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Name"}),
        }
    nickname =forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nickname"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        try:
            models.User.objects.get(nickname=nickname)
            raise  forms.ValidationError("already nickname")
        except models.User.DoesNotExist:
            return  nickname

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        nickname =self.cleaned_data.get("nickname")
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.nickname = nickname
        user.save()