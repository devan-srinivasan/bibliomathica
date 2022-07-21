import json
from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Resource
from bibliomath.managers.topic_manager import TopicsManager
from bibliomath.managers.resource_manager import ResourceManager
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bibliomath.managers.puzzle_manager import PuzzleManager

# MANAGERS
TOPIC_MGR = TopicsManager()
RESOURCE_MGR = ResourceManager()
PUZZLE_MGR = PuzzleManager()

# Create your views here.

# new view for collections
class ResourceListView(ListView):
    model = Resource
    template_name = 'bibliomath/sudo.html'
    context_object_name = 'resources'

class ResourceDetailView(DetailView):
    model = Resource

class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['title', 'description', 'link', 'topic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resource
    fields = ['title', 'description', 'link', 'topic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resource = self.get_object()
        
        return True
    # def test_func(self):
    #     resource = self.get_object()
    #     if self.request.user == resource.author:
    #         return True
    #     return False

class ResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    success_url = '/sudo/'

    def test_func(self):
        resource = self.get_object()
        
        return True
    
# ends here

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
    result = RESOURCE_MGR.add_resource({'topic': res_topic, 'title': res_title, 'description': res_description, 'link': res_link})
    if result:
        return redirect(f'/explore?topic={res_topic}')
    else:
        context = {
            'error': 'attempt to add duplicate resource'
        }
        return render(request, 'bibliomath/error.html', context)

def create_topic(request):
    top_title = request.POST.get('title', '')
    top_description = request.POST.get('description', '')
    result = TOPIC_MGR.add_topic({'title': top_title, 'description': top_description})
    if result:
        context = {
            'topics': TOPIC_MGR.get_topics(),
        }
        return render(request, 'bibliomath/explore.html', context)
    else:
        context = {
            'error': 'attempt to add duplicate topic'
        }
        return render(request, 'bibliomath/error.html', context)

# TODO delete eventually? or style better
def create_puzzle(request):
    p_title = request.POST.get('title', '')
    p_question = request.POST.get('question', '')
    p_answer = request.POST.get('answer', '')
    result = PUZZLE_MGR.add_puzzle({'title': p_title, 'question': p_question, 'answer': p_answer})
    if result:
        return render(request, 'bibliomath/puzzle.html')
    else:
        context = {
            'error': 'attempt to add duplicate puzzle'
        }
        return render(request, 'bibliomath/error.html', context)

def get_all_puzzles(request):
    return JsonResponse(json.dumps(PUZZLE_MGR.get_all_puzzles()), safe=False)

def check_answer(request):
    p_title = request.POST.get('title', '')
    p_submitted_answer = request.POST.get('answer', '')
    answer = PUZZLE_MGR.get_answer(p_title)
    if p_submitted_answer == answer:        # TODO can allow for similar answers not char-by-char correctness
        return JsonResponse(json.dumps({"result": "True"}))
    else:
        return JsonResponse(json.dumps({"result": "False"}))
    