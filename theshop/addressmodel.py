from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

BASE_ADDRESS_TEMPLATE = \
_("""
Name: %(name)s,
Address: %(address)s,
Postal-Code: %(postalcode)s,
City: %(city)s,
Province: %(province)s,
""")

ADDRESS_TEMPLATE = getattr(settings, 'SHOP_ADDRESS_TEMPLATE',
                           BASE_ADDRESS_TEMPLATE)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class MyAddress(models.Model):
    user_shipping = models.OneToOneField(USER_MODEL, related_name='address_shipping',
                                         blank=True, null=True)
    user_billing = models.OneToOneField(USER_MODEL, related_name='address_billing',
                                        blank=True, null=True)

    name = models.CharField(_('Name'), max_length=255)
    address = models.CharField(_('Address'), max_length=255)
    address2 = models.CharField(_('Address2'), max_length=255, blank=True)
    postal_code = models.CharField(_('Postal Code'), max_length=20)
    city = models.CharField(_('City'), max_length=20)
    province = models.CharField(_('Province'), max_length=255)

    class Meta(object):
        verbose_name = _('Address')
        verbose_name_plural = _("Addresses")

    def __unicode__(self):
        return '%s (%s, %s)' % (self.name, self.postal_code, self.city)

    def clone(self):
        new_kwargs = dict([(fld.name, getattr(self, fld.name))
                           for fld in self._meta.fields if fld.name != 'id'])
        return self.__class__.objects.create(**new_kwargs)

    def as_text(self):
        return ADDRESS_TEMPLATE % {
            'name': self.name,
            'address': '%s\n%s' % (self.address, self.address2),
            'postalcode': self.postal_code,
            'city': self.city,
            'province': self.province,
    }