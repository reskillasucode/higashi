from django.contrib import admin
from django.urls import path, include
from ppss.views import payment_list, payment_method_list, invoice_list, customer_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', payment_list, name='payment_list'),
    path('payment-methods/', payment_method_list, name='payment_method_list'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('customers/', customer_list, name='customer_list'),
    path('', payment_list, name='home'),
]
