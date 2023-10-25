from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'is_active', 
                  'is_staff', 
                  'is_superuser', 
                  'password1', 
                  'password2', )
        
class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'is_active', 
                  'is_staff', 
                  'is_superuser', 
                  'password', )