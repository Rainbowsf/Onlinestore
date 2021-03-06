from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView, View
from urllib import request, response
from django.views.generic.edit import FormMixin
from cart.forms import CartAddProductForm


class CategoryListView(ListView):
    """
        Представление списка категорий
    """
    model = Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    """
        Представление списка товаров одной категории
    """
    model = Category
    template_name = 'shop/product-list.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['product_list'] = Product.objects.filter(available=True, category=self.object).order_by('price')
        return context


class ProductDetailView(DetailView, FormMixin):
    """
        Представление товара
    """
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product_detail'
    form_class = CartAddProductForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context


def contacts(request):
    """
        Представление странцы с контактами
    """
    return render(request, 'shop/contacts.html')


def about(request):
    """
        Представление странцы о нас
    """
    return render(request, 'shop/about.html')


def delivery(request):
    """
        Представление странцы доставки
    """
    return render(request, 'shop/delivery.html')


def make_order(request):
    """
        Представление странцы с информацией о персональных заказах
    """
    return render(request, 'shop/make_order.html')

