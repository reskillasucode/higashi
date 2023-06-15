from django import forms
from .models import Customer, Invoice, PaymentMethod, Company

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'email', 'company']

class InvoiceForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None)
    payment_method = forms.ModelChoiceField(queryset=PaymentMethod.objects.all(), empty_label=None)

    class Meta:
        model = Invoice
        fields = ['company', 'amount', 'invoice_date', 'invoice_number', 'payment_method']
