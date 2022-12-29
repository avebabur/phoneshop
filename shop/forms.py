from django import forms
from django.forms import ModelForm
from .models import Phone

"""class PhoneForm(forms.Form):
    name = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    boolean = forms.BooleanField(required=False)
    price = forms.FloatField()
    image = forms.ImageField()
    rubric = forms.CharField(widget=forms.ModelChoiceField(**kwargs))"""

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'