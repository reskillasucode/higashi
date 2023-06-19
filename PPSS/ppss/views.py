from django import forms
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Payment, Customer, Invoice, PaymentMethod, Company
from .forms import InvoiceForm, CustomerForm

# 以下略

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

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'ppss/invoice_create.html', {'form': form})


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'ppss/company_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
    return render(request, 'ppss/customer_create.html', {'form': form})

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'ppss/customer_create.html'
    success_url = '/'
