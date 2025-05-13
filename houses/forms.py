from django import forms
from .models import BookingRequest
from .models import Property
from .models import HouseRequest
from .models import RequestForm


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = '__all__'



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class HouseRequestForm(forms.ModelForm):
    class Meta:
        model = HouseRequest
        fields = ['check_in', 'check_out', 'name', 'phone', 'people_count', 'criteria', 'budget']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите Ваш телефон'}),
            'people_count': forms.NumberInput(attrs={'placeholder': 'Количество человек'}),
            'criteria': forms.TextInput(attrs={'placeholder': 'Ваши критерии к коттеджу'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Допустимый бюджет'}),
        }




class RequestFormForm(forms.ModelForm):
    class Meta:
        model = RequestForm
        fields = ['check_in', 'check_out', 'name', 'phone', 'guests', 'criteria', 'budget']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваш телефон'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество человек'}),
            'criteria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваши критерии к коттеджу'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Допустимый бюджет'}),
        }