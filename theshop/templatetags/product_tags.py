from django.template import Library
from shop.models import Product

register = Library()

@register.inclusion_tag('shop/recent_products.html')
def get_recent_products():
	products = Product.objects.filter().order_by('-date_added')[:1]
	return {'products': products}