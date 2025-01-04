from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room, Customer, Employee

# User Sign-Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email field is added

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields for user creation

# Room Form
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # This includes all fields in the Room model

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # This includes all fields in the Customer model
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # This includes all fields in the Employee model
