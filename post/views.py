from django.shortcuts import HttpResponse, render, redirect
from datetime import date
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryForm, ReviewForm


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
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )

        context = {
            'product': product,
            'review': product.reviews.all(),
            'form': ReviewForm
        }
        return render(request, 'products/product_detail.html', context=context)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={
            'categories': categories
        })


def product_create(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect("/products/")

        context = {
            "form": form
        }

        return render(request, 'products/create.html', context=context)


def category_create(request):
    if request.method == "GET":
        context = {
            'form': CategoryForm
        }
        return render(request, 'products/create_category.html', context)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')

        context = {
            'form': form
        }
        return render(request, 'products/create_category.html', context)
