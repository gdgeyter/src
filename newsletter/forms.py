from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        emailbase, provider = email.split('@')
        domain, extension = email.split('.')
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .edu email adress")
        return email

    def clean_full_name(self):
        full_name =  self.cleaned_data.get('full_name')
        # enter validation code
        return full_name