from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('product/', views.product, name="product"),
	#path('product/<str:pk>', views.product, name="product"),
	path('checkout/', views.checkout, name="checkout"),
	#path('checkout/<str:pk>', views.checkout, name="checkout"),

]
