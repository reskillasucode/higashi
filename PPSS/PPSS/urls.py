from django.contrib import admin
from django.urls import path, include
from ppss.views import payment_list, payment_method_list, invoice_list, customer_list, CompanyCreateView, CustomerCreateView, create_invoice, company_list, BankAccountCreateView, BankAccountRecipientCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', payment_list, name='payment_list'),
    path('payment-methods/', payment_method_list, name='payment_method_list'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('customers/', customer_list, name='customer_list'),
    path('company/create/', CompanyCreateView.as_view(), name='company_create'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('invoice/create/', create_invoice, name='invoice_create'),  
    path('companies/', company_list, name='company_list'),
    path('bank-account/create/', BankAccountCreateView.as_view(), name='bank_account_create'),
    path('bank-account-recipient/create/', BankAccountRecipientCreateView.as_view(), name='payee_account_create'),  
    path('', payment_list, name='home'),
]
