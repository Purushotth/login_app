from django import forms

class LoginForm(forms.Form):
        Last_Name = forms.CharField(label='Last_Name', max_length=45, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name':'Last_Name', 'id': 'Last_Name', 'autocomplete': False, 'placeholder': 'Last_Name', 'required': True}))
        EmailID = forms.CharField(label='EmailID', max_length=254, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'name':'EmailID','id': 'txtEmail', 'autocomplete': False, 'placeholder': 'EmailID', 'required': True}))
        SSN = forms.CharField(label='SSN', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name':'SSN','id': 'txtSSN', 'autocomplete': False, 'placeholder': 'SSN', 'required': True, 'type': 'number'}))

class LogoutForm(forms.Form):
        Last_Name = forms.CharField(label='Last_Name', max_length=45, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name':'Last_Name', 'id': 'Last_Name', 'autocomplete': False, 'placeholder': 'Last_Name', 'required': True}))
        EmailID = forms.CharField(label='EmailID', max_length=254, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'name':'EmailID','id': 'txtEmail', 'autocomplete': False, 'placeholder': 'EmailID', 'required': True}))
        SSN = forms.CharField(label='SSN', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name':'SSN','id': 'txtSSN', 'autocomplete': False, 'placeholder': 'SSN', 'required': True, 'type': 'number'}))

