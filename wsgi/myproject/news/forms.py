from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())


class SignForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone No.', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
    c_password = forms.CharField(label='Re-Type Password', max_length=100, widget=forms.PasswordInput())
