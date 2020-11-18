from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('',views.store, name='store'),
	path('product/<str:pk>/', views.product, name='product'),
	path('checkout/<str:pk>/', views.checkout, name='checkout'),
	path('check/', views.createpost, name='check'),
	path('search/', views.search, name='search'),

]


