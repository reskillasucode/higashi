from django.shortcuts import render
from django.views.generic import CreateView
from .models import Payment, Customer, Invoice, PaymentMethod, Company

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'ppss/payment_list.html', {'payments': payments})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'ppss/customer_list.html', {'customers': customers})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'ppss/invoice_list.html', {'invoices': invoices})

def payment_method_list(request):
    payment_methods = PaymentMethod.objects.all()
    return render(request, 'ppss/payment_method_list.html', {'payment_methods': payment_methods})

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'ppss/company_create.html'
    success_url = '/'