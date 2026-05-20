from django.shortcuts import render
from .models import Product, MonthlyPrice
from django.db.models import Q


def normalize(prices):
    prices = list(prices)
    while len(prices) < 5:
        prices.append(0)
    return prices

def meat_rice_view(request):
    meat_products = Product.objects.filter(category='meat')
    rice_products = Product.objects.filter(category='rice')

    months = ["Yan", "Fev", "Mar", "Apr", "May"]

    def get_prices(products):
        data = []
        for p in products:
            prices = p.prices.order_by('month').values_list('price', flat=True)
            data.append(normalize(prices))
        return data

    context = {
        "months": months,
        "meat": get_prices(meat_products),
        "rice": get_prices(rice_products),
    }

    return render(request, 'dashboard/meat_rice.html', context)


def milk_view(request):
    milk_products = Product.objects.filter(category='milk')

    months = ["Yan", "Fev", "Mar", "Apr", "May"]

    data = []

    for p in milk_products:
        prices = p.prices.order_by('month').values_list('price', flat=True)
        clean_prices = [float(x) for x in prices]
        data.append(normalize(clean_prices))

    return render(request, 'dashboard/milk.html', {
        "months": months,
        "milk": data
    })