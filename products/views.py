from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from .forms import ProductsSearch


       
def home_products(request):
    products = Product.objects.all()
    return render(request, "home_products.html", {"products": products })

def all_products(request, category=""):
    search_form  = ProductsSearch()
    products = Product.objects.all()

    # declare the min price and max price for the initial price filter bar
    min_price=1
    max_price=99

    # Display all products
    if request.GET.get('search_terms'):
        product1=request.GET.get('search_terms')
        products = products.filter(name__contains=product1.capitalize())
    
    if category != "":
        products = products.filter(category__category__exact=category)
   
      # filter products based on min price
    if request.GET.get('min_price'):
        products = products.filter(price__gte=request.GET.get('min_price'))
        min_price=request.GET.get('min_price')
    
   # filter products based on max price
    if request.GET.get('max_price'):
        products = products.filter(price__lte=request.GET.get('max_price'))
        max_price=request.GET.get('max_price')

    '''paginator = Paginator(all_products, 8) # Show 8 products per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)'''
    
    return render(request, "all_products.html",{ 
        "products": products,
        'search_products':search_form,
        'min_price':min_price,
        'max_price':max_price
        })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request,
                  'product_detail.html', {'product': product}) 
