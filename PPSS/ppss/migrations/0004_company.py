# Generated by Django 4.2 on 2023-06-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppss', '0003_alter_payment_status_paymentreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
