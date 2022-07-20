from pydoc_data.topics import topics
import re
from django.shortcuts import render
from .models import Resource
from bibliomath.topics import TopicsList
from bibliomath.helper import jsonify

# TOPICS
TOPIC_LIST = TopicsList()

# Create your views here.
def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    topic = request.GET.get('topic','')
    if not topic == "":
        # do some database stuff
        query_set = Resource.objects.filter(topic=topic)
        resources = jsonify(query_set)
        context = {
            'title': topic,
            'resources': resources,
        }
        return render(request, 'bibliomath/topic.html', context)
    else:
        context = {
            'topics': TOPIC_LIST.get_topics(),
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