from django import forms
from visitor_app.models import *

class VisitForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Visitor.objects.all())
        
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Phone"
        })
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )
    visit_to = forms.ModelChoiceField(queryset=VisitFor.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    purpose = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "purpose"
        })
    )
    