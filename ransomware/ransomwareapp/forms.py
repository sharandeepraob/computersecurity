from django import forms

class MyForm(forms.Form):
    System_Name = forms.CharField(max_length=100)
    Number_Of_Files_Encrypted = forms.CharField(max_length=100)
    Volume_Of_Files = forms.CharField(max_length=500)
    User_Entry_Password = forms.CharField(max_length=100)
    
