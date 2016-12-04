from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Category'), max_length=64)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 verbose_name=_('Category'),
                                 on_delete=models.SET_NULL,
                                 blank=False,
                                 null=True,)
    name = models.CharField(_('Product name'), max_length=128)
    price = models.DecimalField(_('Unit price'), max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u"{name} {price} {category}".format(name=self.name, price=self.price, category=self.category)

#
# Pizza.objects.all().prefetch_related('toppings')
#


class Topping(models.Model):
    name = models.CharField(max_length=30)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __unicode__(self):
        return u"%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
