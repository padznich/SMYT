from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField('Category', max_length=64)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Group')
    name = models.CharField('Product name', max_length=128)
    price = models.DecimalField('Unit price', max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u"{name} {price} {category}".format(name=self.name, price=self.price, category=self.category)
