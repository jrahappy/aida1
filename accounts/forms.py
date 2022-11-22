from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'email', 'username', }


class CustomUserChangeForm(UserChangeForm):

    # department = forms.ModelChoiceField(queryset = get_user_model().objects.all(), initial = 0)
    WORKING_DEPARTMENT = [
        ('SALES', 'Sales'),
        ('MARKE', 'Marketing'),
        ('ACCOU', 'Accounting'),
        ('MANUF', 'Manufacturing'),
        ('PLANN', 'Planning'),
    ]
    department = forms.ChoiceField(choices=WORKING_DEPARTMENT)

    class Meta:
        model = get_user_model()
        fields = {
            'email',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'department',
            'sales_area',
        }
