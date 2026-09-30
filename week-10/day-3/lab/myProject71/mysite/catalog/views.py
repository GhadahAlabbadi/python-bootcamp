from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from .models import Product


@require_GET
def product_list(request):
    products = Product.objects.filter(is_active=True, quantity__gt=0).order_by("category", "name")
    data = [
        {"id": p.pk, "name": p.name, "code": p.code, "category": p.category,
         "price": str(p.price), "quantity": p.quantity}
        for p in products
    ]
    return JsonResponse({"products": data})


@require_GET
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({
        "id": product.pk, "name": product.name, "code": product.code,
        "category": product.category, "price": str(product.price),
        "quantity": product.quantity, "is_active": product.is_active,
    })


def product_dashboard(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "deactivate_category":
            category = request.POST.get("category")
            valid_categories = dict(Product.Category.choices)
            if category in valid_categories:
                updated = Product.objects.filter(category=category).update(is_active=False)
                messages.success(request, f"Deactivated {updated} product(s) in '{category}'.")
            else:
                messages.error(request, "Unknown category.")

        elif action == "cleanup":
            deleted_count, _ = Product.objects.filter(is_active=False, quantity=0).delete()
            messages.success(request, f"Deleted {deleted_count} discontinued product(s).")

        return redirect("catalog:product_dashboard")

    products = Product.objects.all().order_by("category", "name")
    return render(request, "catalog/product_dashboard.html", {
        "products": products,
        "categories": Product.Category.choices,
    })