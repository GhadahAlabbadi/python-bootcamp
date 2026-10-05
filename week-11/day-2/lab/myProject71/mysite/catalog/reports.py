from django.db.models import Avg, Count, Sum

from .models import Product


def category_report():
    return (
        Product.objects.filter(is_active=True)
        .values("category")
        .annotate(
            product_count=Count("pk"),
            average_price=Avg("price"),
            total_stock=Sum("quantity"),
        )
        .filter(product_count__gte=3)
        .order_by("-product_count", "category")
    )


def overall_summary():
    return Product.objects.filter(is_active=True).aggregate(
        total_products=Count("pk"),
        average_price=Avg("price"),
    )