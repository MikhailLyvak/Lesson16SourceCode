from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model

from .models import CustomUser
from django.contrib.auth.forms import SetPasswordForm

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "emailfloatingInput",
                "placeholder": "Введіть ваши email"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "emailfloatingInput",
            "placeholder": "Ввeдіть ваш Нікнейм",
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "passwordfloatingInput",
                "placeholder": "Введіть ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "passwordfloatingInput",
                "placeholder": "Повторіть введений вами пароль",
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "emailfloatingInput",
                "placeholder": "Enter your email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "passwordfloatingInput",
                "placeholder": "Enter your password",
            }
        )
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        if email and password:
            users = CustomUser.objects.all().values_list("email", flat=True)
            user = authenticate(email=email, password=password)
            
            if email not in users:
                raise ValidationError("Введений Вами логін (емейл) не зареєстрований в системі!")
            if user is None or not user.is_active:
                raise ValidationError("Введний Вами пароль не вірний!")
            
        return cleaned_data
    
    def get_authenticated_user(self):
        email = self.cleaned_data.get("email")
        return authenticate(email=email, password=self.cleaned_data.get("password"))
