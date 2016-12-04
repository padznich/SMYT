from django.shortcuts import render
from django.db.models import Count

from models import Product


def show_home_page(request):

    a1 = Product.objects.select_related('category').get(id=1)
    q1 = a1.price  # a1.category
    q2 = Product.objects.all()

    print "-" * 100
    for p in Product.objects.all():
        print p.category.name, p.name, p.price

    context = {'q1': q1, 'q2': q2}

    return render(request, 'index.html', context)
