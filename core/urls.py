from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:item_id>/single_item/',views.single_item,name='single_item'),
    path('add_item',views.add_item,name='add_item'),
    path('<int:item_id>/edit_item',views.edit_item,name='edit_item'),
    path('<int:item_id>/delete_item',views.delete_item,name='delete_item'),
    path('browse_items',views.browse_items,name='browse_items'),
    path('browse_items/<int:category_id>/',views.browse_items,name='browse_category'),
    path('my_items/<int:user_id>/',views.my_items,name='my_items'),
    path('register',views.register,name='register')
]