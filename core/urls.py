from django.urls import path
from core.views import item_detail, get_checkout_session, success_page_view, cancel_page_view

urlpatterns = [
    path('buy/<int:item_id>/', get_checkout_session, name='create_checkout_session'),
    path('item/<int:item_id>/', item_detail, name='show_item_page'),
    path('success/<int:item_id>/', success_page_view, name='success_page'),
    path('cancel/<int:item_id>/', cancel_page_view, name='cancel_page'),
]
