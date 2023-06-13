from django.contrib import admin
from django.db import models
from .models import Payment, Customer, Invoice, PaymentMethod, BankAccount, PaymentReview

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'amount', 'payment_date', 'payment_method', 'status', 'bank_account_from', 'bank_account_to')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(PaymentMethod)
admin.site.register(BankAccount)
admin.site.register(PaymentReview)