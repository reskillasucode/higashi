# Generated by Django 4.2 on 2023-06-15 08:39

from django.db import migrations, models
import django.db.models.deletion
import ppss.models


class Migration(migrations.Migration):

    dependencies = [
        ('ppss', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(default=ppss.models.get_default_company, on_delete=django.db.models.deletion.CASCADE, to='ppss.company'),
        ),
    ]
