import decimal
from shop.cart.cart_modifiers_base import BaseCartModifier

class Fixed14PercentTaxRate(BaseCartModifier):
	"""Adds the standard 14percent tax"""

	def get_extra_cart_price_field(self, cart, request):
		taxes = decimal.Decimal('0.14') * cart.subtotal_price
		to_append = ('Taxes total', taxes)
		return to_append