from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__' #all the fields will be shown in the employee_form.html
        fields = ('fullname', 'mobile', 'email', 'position') #customized fields

        #CUSTOMIZED LABELS (CRISPY_FORMS)
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Email',
        }


    ##For Changing the label of select menu of position
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['position'].empty_label = "Select"

        self.fields['email'].required = True
