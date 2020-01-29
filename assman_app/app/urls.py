from django.urls import path
from . import views

urlpatterns = [
	# Item urls
	path('', views.ItemList.as_view(), name='item_list'),
	path('view_item/item_<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
	path('new_item', views.ItemCreate.as_view(), name='item_new'),
	path('edit/item_<int:pk>', views.ItemUpdate.as_view(), name='item_edit'),
	path('delete/item_<int:pk>', views.ItemDelete.as_view(), name='item_delete'),
	path('item_search', views.ItemSearchResultsView.as_view(), name='item_search_results'),

	# Key urls
	path('key_list', views.KeyList.as_view(), name='key_list'),
	path('view_key/key_<int:pk>', views.KeyDetail.as_view(), name='key_detail'),
	path('new_key', views.KeyCreate.as_view(), name='key_new'),
	path('edit/key_<int:pk>', views.KeyUpdate.as_view(), name='key_edit'),
	path('delete/key_<int:pk>', views.KeyDelete.as_view(), name='key_delete'),
	path('key_search', views.KeySearchResultsView.as_view(), name='key_search_results'),

	# Card urls
	path('card_list', views.CardList.as_view(), name='card_list'),
	path('view_card/card_<int:pk>', views.CardDetail.as_view(), name='card_detail'),
	path('new_card', views.CardCreate.as_view(), name='card_new'),
	path('edit/card_<int:pk>', views.CardUpdate.as_view(), name='card_edit'),
	path('delete/card_<int:pk>', views.CardDelete.as_view(), name='card_delete'),
	path('card_search', views.CardSearchResultsView.as_view(), name='card_search_results')

]