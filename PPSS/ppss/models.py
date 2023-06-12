from django.db import models

class Payment(models.Model):
    # 支払いに関するフィールドを定義。顧客情報、支払金額、支払日、支払方法、ステータス、メモフィールド
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    payment_date = models.DateField()
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.PROTECT)
    status = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'Payment: {self.id}'

class Customer(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Invoice(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=20)

    def __str__(self):
        return self.invoice_number

class PaymentMethod(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('窓口', '窓口'),
        ('インターネットバンキング', 'インターネットバンキング'),
        ('Pay-easy', 'Pay-easy'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    def __str__(self):
        return self.invoice_number



