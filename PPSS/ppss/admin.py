from django.contrib import admin
from .models import Payment, Customer, Invoice, PaymentMethod

admin.site.register(Payment)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(PaymentMethod)
