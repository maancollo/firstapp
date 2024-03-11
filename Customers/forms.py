from django import forms
from .models import Registrations
from Customers.models import CustomersComplain

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=True,label = "enter your name")
    age = forms.IntegerField(min_value =18,
                             label = "enter your age"),
    check= forms.BooleanField(required= False,
                              label = "check if"),
    category = forms.ChoiceField(choices = [('student','student'),
                                            ('teacher','teacher')]),




class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = CustomersComplain
        fields = ['name', 'email']


class RegisterForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=9)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
         password = forms.CharField(widget=forms.PasswordInput)
         class Meta:
          model = Registrations
          fields = ['first_name', 'last_name', 'email', 'password']