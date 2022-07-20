from pydoc_data.topics import topics
import re
from django.shortcuts import render
from .models import Resource
from bibliomath.topics import TopicsList

# TOPICS
TOPIC_LIST = TopicsList()

# Create your views here.
def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    context = {
        'topics': TOPIC_LIST.get_topics(),
    }
    return render(request, 'bibliomath/explore.html', context)

def collection(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    resources = [
        {  
            'title': 'Colliding Masses', 
            'description': 'Why do the number of collisions between colliding masses, all powers of ten, spit out the digits of pi?',
            'link': 'https://www.youtube.com/watch?v=jsYwFizhncE',
            'complete': False,
            'favourite': True,
        }
    ] * 3
    context = {
        'resources': resources,
    }
    return render(request, 'bibliomath/collection.html', context)

def create(request):
    res_topic = request.GET.get('topic', '')
    res_title = request.GET.get('title', '')
    res_description = request.GET.get('description', '')
    res_link = request.GET.get('link', '')
    new_resource = Resource(title=res_title, description=res_description, link=res_link, topic=res_topic)
    new_resource.save()
    context = {
        'topics': TOPIC_LIST.get_topics(),
    }
    print(context)
    return render(request, 'bibliomath/explore.html', context)