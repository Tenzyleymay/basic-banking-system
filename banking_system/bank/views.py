from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Transfer
from django.db.models import F

def home(request):
    return render(request, 'bank/home.html')

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'bank/customers.html', {'customers': customers})

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'bank/customer_detail.html', {'customer': customer})


def aboutus(request):
    return render(request, 'bank/aboutus.html')

def transfer(request, customer_id):
    sender = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        receiver_id = request.POST['receiver']
        amount = request.POST['amount']
        receiver = get_object_or_404(Customer, id=receiver_id)
        if sender.current_balance >= float(amount):
            sender.current_balance = F('current_balance') - amount
            receiver.current_balance = F('current_balance') + amount
            sender.save()
            receiver.save()
            Transfer.objects.create(sender=sender, receiver=receiver, amount=amount)
            return redirect('customers')
        else:
            return render(request, 'bank/transfer.html', {'sender': sender, 'error': 'Insufficient balance'})
    customers = Customer.objects.exclude(id=sender.id)
    return render(request, 'bank/transfer.html', {'sender': sender, 'customers': customers})

