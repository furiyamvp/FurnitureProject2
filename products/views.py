from django.shortcuts import render
from products.models import *


def products_page_view(request):
    cat = request.GET.get('cat')
    products = ProductModel.objects.all().order_by('-pk')
    categories = CategoryModel.objects.all().order_by('-pk')
    companies = CompanyModel.objects.all().order_by('-pk')
    tags = TagModel.objects.all().order_by('-pk')
    colors = ColorModel.objects.all().order_by('-pk')

    if cat:
        products = products.filter(categories=cat)
    context = {
        "products": products,
        "categories": categories,
        "companies": companies,
        "tags": tags,
        "colors": colors,
    }
    return render(request, 'product-list.html', context)
