from django.shortcuts import HttpResponse, render
from datetime import date
from post.models import Product, Category


def main_view(request):
    products = Product.objects.all()
    return render(request, 'index.html')


def current_date_view(request):
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return HttpResponse(f"Today's date: {formatted_date}")


def goodbye_view(request):
    return HttpResponse('Goodbye user! ﾐ🎀・◦・ﾐ')


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', context={
        'products': products
    })


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'products/categories.html', context={
        'categories': categories
    })

