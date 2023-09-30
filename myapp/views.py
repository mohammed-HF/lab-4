from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
   
def index(request):
    return HttpResponse("this is a site to calculate tax")

def calculate_total_price(request, number):
    tax_rate = Decimal("0.15")
    total_price = number + (number * tax_rate)
    response_text = f"The total for {number} with tax will be {total_price}"
    return HttpResponse(response_text)


def display_tax_rate(request):
    tax_rate = Decimal('0.15')
    return render(request, 'taxrate.html', {'tax_rate': tax_rate})

