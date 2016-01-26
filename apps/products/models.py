from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models

class Product(models.Model):
	description = models.TextField(max_length=50)
	price = models.FloatField()
	created_at = models.DateTimeField(default = datetime.now())
	updated_at = models.DateTimeField(default = datetime.now())
	def __str__(self):
		return self.description
	class Meta:
		db_table = 'products'

class User(models.Model):
	name = models.TextField(max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'users'

class Cart(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	qty = models.IntegerField()

	def __str__(self):
		return self.user
	class Meta:
		db_table = 'carts'