from django.core import validators
from django import forms
from . models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['code', 'person_type', 'fname', 'father', 'lname', 'religion', 'sex', 'nation', 'age']
