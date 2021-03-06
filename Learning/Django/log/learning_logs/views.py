from django.shortcuts import render
# Create your views here.
from .models import Topic

def index(request):
	"""The home page for learning logs"""
	return render(request, 'learning_logs/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	#Show a single topic and all it's entries.
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)