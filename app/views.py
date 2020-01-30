from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django import forms

from .models import Key
from .models import Card
from .models import Item
from .models import Bin

# Custom item form class
class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['item_name', 'item_location', 'item_qty', 'item_longdescription']
		widgets = {
			'item_longdescription' : forms.Textarea()
		}
		
# Items views
class ItemList(ListView):
	model = Item

class ItemDetail(DetailView):
	model = Item

class ItemCreate(CreateView):
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('item_list')

class ItemUpdate(UpdateView):
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('item_list')

class ItemDelete(DeleteView):
	model = Item
	success_url = reverse_lazy('item_list')

class ItemSearchResultsView(ListView):
	model = Item
	template_name = 'app/item_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Item.objects.filter(
				Q(item_name__icontains=query) | Q(item_longdescription__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Keys views
class KeyList(ListView):
	model = Key

class KeyDetail(DetailView):
	model = Key

class KeyCreate(CreateView):
	model = Key
	fields = ['key_name', 'key_location', 'key_owner']
	success_url = reverse_lazy('key_list')

class KeyUpdate(UpdateView):
	model = Key
	fields = ['key_name', 'key_owner', 'key_location']
	success_url = reverse_lazy('key_list')

class KeyDelete(DeleteView):
	model = Key
	success_url = reverse_lazy('key_list')

class KeySearchResultsView(ListView):
	model = Key
	template_name = 'app/key_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Key.objects.filter(
				Q(key_name__icontains=query) | Q(key_owner__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Cards views
class CardList(ListView):
	model = Card

class CardDetail(DetailView):
	model = Card

class CardCreate(CreateView):
	model = Card
	fields = ['card_name', 'card_owner', 'card_location']
	success_url = reverse_lazy('card_list')

class CardUpdate(UpdateView):
	model = Card
	fields = ['card_name', 'card_owner', 'card_location']
	success_url = reverse_lazy('card_list')

class CardDelete(DeleteView):
	model = Card
	success_url = reverse_lazy('card_list')

class CardSearchResultsView(ListView):
	model = Card
	template_name = 'app/card_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Card.objects.filter(
				Q(card_name__icontains=query) | Q(card_owner__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


class BinForm(forms.ModelForm):
	class Meta:
		model = Bin
		fields = ['bin_name', 'bin_location', 'bin_contents' ]
		widgets = {
			'bin_contents' : forms.Textarea()
		}

# Items views
class BinList(ListView):
	model = Bin

class BinDetail(DetailView):
	model = Bin

class BinCreate(CreateView):
	model = Bin
	form_class = BinForm
	success_url = reverse_lazy('bin_list')

class BinUpdate(UpdateView):
	model = Bin
	form_class = BinForm
	success_url = reverse_lazy('bin_list')

class BinDelete(DeleteView):
	model = Bin
	success_url = reverse_lazy('bin_list')

class BinSearchResultsView(ListView):
	model = Bin
	template_name = 'app/bin_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Bin.objects.filter(
				Q(bin_name__icontains=query) | Q(bin_contents__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")
