from django.shortcuts import render

# Create your views here.
def index(request):
	"""The home page for the pizzeria project."""
	return render(request, 'pizzas/index.html')