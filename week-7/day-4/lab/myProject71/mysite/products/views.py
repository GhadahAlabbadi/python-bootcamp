from django.shortcuts import render
from django.http import Http404

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'category': 'electronics', 'price': 19.99,
     'rating': 4.2, 'description': 'A smooth, responsive wireless mouse with a 6-month battery life.'},
    {'id': 2, 'name': 'Mechanical Keyboard', 'category': 'electronics', 'price': 59.99,
     'rating': 4.6, 'description': 'Tactile mechanical keyboard with RGB backlighting and hot-swappable switches.'},
    {'id': 3, 'name': 'Running Shoes', 'category': 'sportswear', 'price': 74.50,
     'rating': 4.0, 'description': 'Lightweight running shoes with breathable mesh and cushioned soles.'},
    {'id': 4, 'name': 'Yoga Mat', 'category': 'sportswear', 'price': 24.99,
     'rating': 4.4, 'description': 'Non-slip yoga mat, 6mm thick, includes a carrying strap.'},
    {'id': 5, 'name': 'Coffee Maker', 'category': 'home', 'price': 89.00,
     'rating': 3.9, 'description': 'Programmable drip coffee maker with a 12-cup glass carafe.'},
    {'id': 6, 'name': 'Blender', 'category': 'home', 'price': 45.75,
     'rating': 4.1, 'description': 'High-speed blender with 3 preset programs and a 1.5L jar.'},
    {'id': 7, 'name': 'Desk Lamp', 'category': 'home', 'price': 15.25,
     'rating': 4.3, 'description': 'Adjustable LED desk lamp with three brightness levels.'},
    {'id': 8, 'name': 'Bluetooth Speaker', 'category': 'electronics', 'price': 34.99,
     'rating': 4.5, 'description': 'Portable Bluetooth speaker with 10 hours of playback.'},
]

PAGE_SIZE = 3
VALID_SORTS = ('price', 'rating', 'name')
VALID_TABS = ('details', 'reviews', 'shipping')


def product_list(request):
    category = request.GET.get('category', '').strip()
    query = request.GET.get('q', '').strip()

    min_price_raw = request.GET.get('min_price', '').strip()
    min_price = None
    if min_price_raw:
        try:
            min_price = float(min_price_raw)
        except ValueError:
            min_price = None

    sort = request.GET.get('sort', 'name').strip()
    if sort not in VALID_SORTS:
        sort = 'name'

    filtered = products
    if category:
        filtered = [p for p in filtered if p['category'] == category]
    if min_price is not None:
        filtered = [p for p in filtered if p['price'] >= min_price]
    if query:
        filtered = [p for p in filtered if query.lower() in p['name'].lower()]

    filtered = sorted(filtered, key=lambda p: p[sort])

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    page = max(page, 1)

    total_pages = max(1, (len(filtered) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = min(page, total_pages)

    start = (page - 1) * PAGE_SIZE
    page_products = filtered[start:start + PAGE_SIZE]

    return render(request, 'products/product_list.html', {
        'products': page_products,
        'category': category,
        'min_price': min_price_raw,
        'query': query,
        'sort': sort,
        'page': page,
        'total_pages': total_pages,
        'has_previous': page > 1,
        'has_next': page < total_pages,
    })


def product_detail(request, id):
    product = next((p for p in products if p['id'] == id), None)
    if product is None:
        raise Http404('Product not found.')

    tab = request.GET.get('tab', 'details')
    if tab not in VALID_TABS:
        tab = 'details'

    return render(request, 'products/product_detail.html', {
        'product': product,
        'tab': tab,
    })