from django.core.exceptions import ValidationError

from newtest.models import Contact,Register
from django import forms
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

    def clean_email(self):
        Email = self.cleaned_data['email']
        if Register.objects.filter(Email=Email).exists():
            raise ValidationError("Email already exists")
        return Email