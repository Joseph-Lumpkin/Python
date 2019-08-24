from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.
def index(request):
	"""The home page for the pizzeria project."""
	return render(request, 'pizzas/index.html')

def pizzas(request):
	#Show the webpage containing all available pizza orders.
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
	#Show a webpage that displays all the toppings asssociated with the pizza
	#selected.
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.order_by('-date_added')
	context = {'pizza':pizza, 'toppings':toppings}
	return render(request, 'pizzas/toppings.html', context)