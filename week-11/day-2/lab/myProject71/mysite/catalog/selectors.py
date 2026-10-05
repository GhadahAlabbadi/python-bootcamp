from django.db.models import Q

from .models import Product


def search_products(query=None, min_price=None, max_price=None, category=None):
    """
    One reusable, chainable QuerySet for searching the product catalog.
    Every argument is optional -- pass only the filters you need.
    """
    qs = Product.objects.filter(is_active=True, quantity__gt=0)

    if query:
        qs = qs.filter(Q(name__icontains=query) | Q(sku__icontains=query))

    if min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if category:
        qs = qs.filter(category__iexact=category)

    return qs.order_by("price", "name", "pk")