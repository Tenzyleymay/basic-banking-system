from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender = models.ForeignKey(Customer, related_name='sent_transfers', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, related_name='received_transfers', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} : {self.amount}'
