# Generated by Django 5.1.6 on 2025-02-28 02:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donor',
            new_name='DonorPerson',
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_donated', models.DecimalField(decimal_places=2, help_text='Amount donated by the donor', max_digits=10)),
                ('transaction_id', models.CharField(blank=True, help_text='Unique transaction ID from payment gateway', max_length=100, null=True, unique=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], default='Pending', help_text='Status of the payment', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Time when donation was made')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
