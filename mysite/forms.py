from django import forms
from .models import Profile

#a form ProfileForm based on the Profile 
# model and including only the location field

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location']