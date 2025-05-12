from django import forms
from .models import BookingRequest
from .models import Property

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = '__all__'



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
