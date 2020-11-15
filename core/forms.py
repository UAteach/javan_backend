from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ExtendedUser
from django import forms

class ExtendedUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ExtendedUser
        fields = ('username', 'email', 'classification', 'first_name', 'last_name')

        def is_school_email(self):
            email = self.cleaned_data.get('email')

            email_exists = ExtendedUser.objects.get(email=email)

            if email_exists:
                raise forms.ValidationError('A user with this email exists.')


class ExtendedUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = ExtendedUser
        fields = ('username', 'email', 'classification')
