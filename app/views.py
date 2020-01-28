from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Key
from .models import Card
from .models import Item

# Items views
class ItemList(ListView):
	model = Item

class ItemDetail(DetailView):
	model = Item

class ItemCreate(CreateView):
	model = Item
	fields = ['item_name', 'item_location', 'item_qty', 'item_longdescription']
	success_url = reverse_lazy('item_list')

class ItemUpdate(UpdateView):
	model = Item
	fields = ['item_name', 'item_location', 'item_qty', 'item_longdescription']
	success_url = reverse_lazy('item_list')

class ItemDelete(DeleteView):
	model = Item
	success_url = reverse_lazy('item_list')


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