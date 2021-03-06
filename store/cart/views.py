from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_id):
    """
        Добавление товара в корзину
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])
    return redirect('cart:cart_added')


def cart_remove(request, product_id):
    """
        Удаление товара из корзины
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """
        Отображение корзины
    """
    cart = Cart(request)
    return render(request, 'cart/cart-detail.html', {'cart': cart})


def cart_added(request):
    return render(request, 'cart/cart-added.html')