from django.urls import path
from . import views

app_name = 'ppss'

urlpatterns = [
    path('payments/', views.payment_list, name='payment_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('payment_methods/', views.payment_method_list, name='payment_method_list'),
]
