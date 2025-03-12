from django.db import models

# Create your models here.
class Transactions(models.Model):
    bill_number = models.IntegerField(unique=True)
    total_amount = models.DecimalField(max_digits = 10, decimal_places=2)
    date = models.DateField()
    amount_paid = models.DecimalField(max_digits = 10, decimal_places=2, default=0)
    
    @property
    def balance_amount(self):
        return self.total_amount - self.amount_paid
    
    def __str__(self):
        return f"Bill Number: {self.bill_number}"
    
    
    
class Payment(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits = 10, decimal_places=2)