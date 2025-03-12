from django.shortcuts import render, redirect
from .models import Transactions, Payment
# from django.views.generic import ListView, CreateView
from .forms import PaymentForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

# class BillListView(ListView):
#     model = Transactions
#     template_name = 'all_bills.html'
#     context_object_name = 'bills'



def get_all_bills(request):
    bills = Transactions.objects.all()
    payments = Payment.objects.all()
    return render(request, 'all_bills.html', {'bills':bills, 'payments':payments})

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            remaining_amount = payment.amount
            bills = [bill for bill in Transactions.objects.all() if bill.balance_amount > 0]
            for bill in bills:
                if remaining_amount <=0:
                    break
                amount_to_pay = min(bill.balance_amount, remaining_amount)
                bill.amount_paid += amount_to_pay
                bill.save()
                remaining_amount -= amount_to_pay
            return redirect('bills')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})