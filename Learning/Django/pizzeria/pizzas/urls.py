from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
		#Home page
		path('', views.index, name='index'),
		
		#Show the pizzas available.
		path('pizzas/', views.pizzas, name='pizzas'),
		
		#Show a list of the toppings available to that specific pizza.
		path('toppings/<int:pizza_id>/', views.toppings, name='toppings'),
	]