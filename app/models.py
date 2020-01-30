from django.db import models

class Item(models.Model):
	item_name = models.CharField(max_length=50)
	item_location = models.CharField(max_length=50)
	item_qty = models.IntegerField(default=1)
	item_longdescription = models.CharField(max_length=300)
	item_id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.item_name

	def get_absolute_url(self):
		return reverse("item_edit", kwargs={"pk": self.pk})
	

class Key(models.Model):
	OWNERS = (
		('r', 'Regent'),
		('vr', 'Vice Regent'), 
		('s', 'Scribe'), 
		('t', 'Treasurer'), 
		('cs', 'Corresponding Secretary'),
		('ig', 'Inner Guard'),
		('og', 'Outer Guard'),
		('m', 'Marshal'),
		('o', 'Other')
	)

	key_name = models.CharField(max_length=20)
	key_owner = models.CharField(max_length=2, choices=OWNERS)
	key_location = models.CharField(max_length=50)
	key_id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.key_name

	def get_absolute_url(self):
		return reverse("key_edit", kwargs={"pk": self.pk})
	

class Card(models.Model):
	OWNERS = (
		('r', 'Regent'),
		('vr', 'Vice Regent'), 
		('s', 'Scribe'), 
		('t', 'Treasurer'), 
		('cs', 'Corresponding Secretary'),
		('ig', 'Inner Guard'),
		('og', 'Outer Guard'),
		('m', 'Marshal'),
		('o', 'Other')
	)

	card_name = models.CharField(max_length=20)
	card_owner = models.CharField(max_length=2, choices=OWNERS)
	card_location = models.CharField(max_length=20)
	card_id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.card_name

	def get_absolute_url(self):
		return reverse("card_edit", kwargs={"pk": self.pk})


class Bin(models.Model):
	bin_name = models.CharField(max_length=20)
	bin_location = models.CharField(max_length=20)
	bin_contents = models.CharField(max_length=200)
	bin_id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.card_name

	def get_absolute_url(self):
		return reverse("bin_edit", kwargs={"pk": self.pk})