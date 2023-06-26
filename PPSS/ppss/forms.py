from django import forms
from .models import Customer, Invoice, PaymentMethod, Company, BankAccount

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

class BankAccountForm(forms.ModelForm):
    branch_number = forms.IntegerField(min_value=0, max_value=999)
    account_number = forms.IntegerField(min_value=0, max_value=9999999)

    def clean_branch_number(self):
        branch_number = self.cleaned_data['branch_number']
        if len(str(branch_number)) != 3:
            raise forms.ValidationError("支店番号は3桁の数字で入力してください。")
        return branch_number

    def clean_account_number(self):
        account_number = self.cleaned_data['account_number']
        if len(str(account_number)) != 7:
            raise forms.ValidationError("口座番号は7桁の数字で入力してください。")
        return account_number

    class Meta:
        model = BankAccount
        fields = '__all__'
