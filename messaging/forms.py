from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'is_staff',
            'is_active',
            'groups',
            'first_name',
            'last_name',
            'email'
        ]