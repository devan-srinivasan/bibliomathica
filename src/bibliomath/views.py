from pydoc_data.topics import topics
import re
import resource
from django.shortcuts import render, redirect
from .models import Resource
from bibliomath.managers.topic_manager import TopicsManager
from bibliomath.managers.resource_manager import ResourceManager

# TOPICS
TOPIC_MGR = TopicsManager()
RESOURCE_MGR = ResourceManager()

# Create your views here.
def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    topic = request.GET.get('topic','')
    if not topic == "":
        # do some database stuff
        resources = RESOURCE_MGR.get_resources_topic(topic)
        context = {
            'title': topic,
            'resources': resources,
        }
        return render(request, 'bibliomath/topic.html', context)
    else:
        context = {
            'topics': TOPIC_MGR.get_topics(),
        }
        return render(request, 'bibliomath/explore.html', context)

def collection(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    resources = []
    context = {
        'resources': resources,
    }
    return render(request, 'bibliomath/collection.html', context)

def create_resource(request):
    res_topic = request.POST.get('topic', '')
    res_title = request.POST.get('title', '')
    res_description = request.POST.get('description', '')
    res_link = request.POST.get('link', '')
    RESOURCE_MGR.add_resource({'topic': res_topic, 'title': res_title, 'description': res_description, 'link': res_link})

    return redirect(f'/explore?topic={res_topic}')

def create_topic(request):
    top_title = request.POST.get('title', '')
    top_description = request.POST.get('description', '')
    TOPIC_MGR.add_topic({'title': top_title, 'description': top_description})
    context = {
        'topics': TOPIC_MGR.get_topics(),
    }
    return render(request, 'bibliomath/explore.html', context)