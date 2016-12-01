from django.shortcuts import render
from django.db.models import Count

from models import Product


def show_home_page(request):

    q1 = Product.objects.filter(price__gte=100).values('category').annotate(total=Count('category'))
    q2 = Product.objects.filter(price__gte=100).values('category').annotate(total=Count('category')).filter(total__gt=10)

    print "-" * 100
    for p in Product.objects.all():
        print p.category.name, p.name, p.price

    context = {'q1': q1, 'q2': q2}

    return render(request, 'home.html', context)