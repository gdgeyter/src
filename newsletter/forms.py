from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required= False)
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name','last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_first_name(self):
        first_name =  self.cleaned_data.get('first_name')
        # enter validation code
        return first_name

    def clean_last_name(self):
        last_name =  self.cleaned_data.get('last_name')
        # enter validation code
        return last_name