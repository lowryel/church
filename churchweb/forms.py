from django.forms import ModelForm
from django import forms
from churchweb.models import Fruit, ContactUs

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    phone = forms.IntegerField(required=False)
    class Meta:
        model = ContactUs
        fields = '__all__'


    def validate_fields(self):
        ...