from django.views.generic import CreateView, ListView
from django import forms
from django.shortcuts import render, redirect
from .models import Payment, Customer, Invoice, PaymentMethod, Company, BankAccount, BankAccountRecipient
from .forms import InvoiceForm, CustomerForm, BankAccountForm, PpssReview

from django.views.generic import ListView
from .models import Company

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

class CompanyListView(ListView):
    model = Company
    template_name = 'ppss/company_list.html'
    context_object_name = 'companies'

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'ppss/company_list.html', {'companies': companies})

class BankAccountCreateView(CreateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'ppss/bank_account_create.html'
    success_url = '/'

class BankAccountRecipientCreateView(CreateView):
    model = BankAccountRecipient
    fields = ['account_number', 'branch_number', 'branch_name', 'account_type']
    template_name = 'ppss/bank_account_recipient_create.html'
    success_url = '/success-url/' 

    def form_valid(self, form):
        return super().form_valid(form)

def ppss_review(request, invoice_id):
    # 対象のInvoiceオブジェクトを取得
    invoice = Invoice.objects.get(id=invoice_id)

    if request.method == 'POST':
        form = PpssReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.invoice = invoice
            review.save()
            return redirect('invoice_detail', invoice_id=invoice_id)
    else:
        form = PpssReviewForm()

    context = {
        'form': form,
        'invoice': invoice,
    }
    return render(request, 'ppss_review.html', context)
