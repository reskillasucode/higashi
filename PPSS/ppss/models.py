from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import PpssReview

class Payment(models.Model):
     # ステータスの選択肢
    STATUS_CHOICES = [
        ('新規', '新規'),
        ('登録中', '登録中'),
        ('申請中', '申請中'),
        ('承認済み', '承認済み'),
        ('支払いデータ作成済み', '支払いデータ作成済み'),
        ('支払済み', '支払済み'),
    ]

    # 支払いに関するフィールドを定義。顧客情報、支払金額、支払日、支払方法、ステータス、メモフィールド
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    payment_date = models.DateField()
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.PROTECT)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    description = models.TextField()
    bank_account_from = models.ForeignKey('BankAccount', on_delete=models.PROTECT, related_name='payments_from', default=None)
    bank_account_to = models.ForeignKey('BankAccount', on_delete=models.PROTECT, related_name='payments_to', default=None)

    def __str__(self):
        return f'Payment: {self.customer}'

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def get_default_company():
    default_company, _ = Company.objects.get_or_create(name='Default Company')
    return default_company.pk


class Customer(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=get_default_company)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Invoice(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=20)
    applied_date=models.DateField(auto_now=True)
    STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
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
        return self.payment_method

class BankAccount(models.Model):
    BANK_CHOICES = [
        ('savings', '普通預金'),
        ('checking', '当座預金'),
        ('others', 'その他')
    ]
        
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=20, default='default_branch_name')
    branch_number = models.PositiveIntegerField(default=000)
    account_number = models.PositiveIntegerField(default=0000000)
    account_holder = models.CharField(max_length=30)
    account_type = models.CharField(max_length=20, choices=BANK_CHOICES)

    def __str__(self):
        return f'{self.bank_name} - {self.account_holder}'

class PaymentReview(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        subject = '支払レビュー依頼'
        message = f'支払いレビューが作成されました。レビュー内容: {self.comment}'
        from_email = 'sender@example.com'
        to_email = 'recipient@example.com'
        send_mail(subject, message, from_email, [to_email])

from django.db import models

class BankAccountRecipient(models.Model):
    BANK_CHOICES = [
        ('savings', '普通預金'),
        ('checking', '当座預金'),
        ('others', 'その他')
    ]
        
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=20, default='default_branch_name')
    branch_number = models.PositiveIntegerField(default=0)
    account_number = models.PositiveIntegerField(default=0)
    account_holder = models.CharField(max_length=30)
    account_type = models.CharField(max_length=20, choices=BANK_CHOICES)

    def __str__(self):
        return self.bank_name

class PpssReview(models.Model):
    comment = models.TextField()
    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.invoice.invoice_number
