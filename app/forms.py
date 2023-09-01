from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ServiceRequest, JobRequest

class BootstrapAuthenticationForm(AuthenticationForm):
    pass

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['pickup_location', 'destination', 'date', 'time']
        # Add more fields as needed

class JobRequestForm(forms.ModelForm):
    class Meta:
        model = JobRequest
        fields = ['pickup_location', 'destination', 'date', 'time', 'driver_accepted']
        # Add more fields as needed

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=20)
