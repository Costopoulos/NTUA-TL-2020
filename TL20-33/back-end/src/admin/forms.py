from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class NewPasswordForm(forms.Form):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Πληκτρολογήστε τον κωδικό πρόσβασής σας','class' : 'form-control','id': 'pwd'})
    )

class UserLoginForm(forms.Form):
    """ User login form """

    user = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Πληκτρολογήστε το όνομα χρήστη σας','class' : 'form-control','id': 'username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Πληκτρολογήστε τον κωδικό πρόσβασής σας','class' : 'form-control','id': 'pwd'})
    )

    def clean_user(self):
        user = self.cleaned_data.get('user')
        r_user = User.objects.filter(username=user)
        if r_user.count() == 0:
            raise  ValidationError("Ο χρήστης δεν βρέθηκε στο σύστημα", code='user_not_exists')
        self.usr = user
        return user

    def clean_password(self):
        user = self.cleaned_data.get('user')
        password = self.cleaned_data.get('password')
        user = authenticate(username=user, password=password)
        #token = Token.objects.get(user=user)
        if user is None:
            raise ValidationError("Λάθος κωδικός πρόσβασης",code='wrong_password')
        return password

        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()