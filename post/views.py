from django.shortcuts import HttpResponse, render
from datetime import date
from post.models import Product, Category, Review


def main_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'index.html')


def current_date_view(request):
    if request.method == 'GET':
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        return HttpResponse(f"Today's date: {formatted_date}")


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user! ﾐ🎀・◦・ﾐ')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'products/products.html', context={
            'products': products
        })


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {
            'product': product
        }
        return render(request,
                      'products/product_detail.html',
                      context=context)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={
            'categories': categories
        })

