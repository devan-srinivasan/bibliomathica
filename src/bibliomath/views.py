import json
from pydoc_data.topics import topics
from turtle import title
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Resource, Topic, Puzzle
from bibliomath.managers.topic_manager import TopicsManager
from bibliomath.managers.resource_manager import ResourceManager
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bibliomath.managers.puzzle_manager import PuzzleManager
from users.models import Collection

# MANAGERS
TOPIC_MGR = TopicsManager()
RESOURCE_MGR = ResourceManager()
PUZZLE_MGR = PuzzleManager()

ERROR = 0.01

# Create your views here.

# new view for sudo
def sudo(request):
    topics = Topic.objects.all()
    resources = Resource.objects.all()
    puzzles = Puzzle.objects.all()

    context = {
        'topics': topics,
        'resources': resources,
        'puzzles': puzzles,
    }
    return render(request, 'bibliomath/sudo.html', context)


class TopicDetailView(DetailView):
    model = Topic
    slug_field = 'title'

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    slug_field = 'title'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        topic = self.get_object()
        
        return True

class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    slug_field = 'title'
    success_url = '/sudo/'

    def test_func(self):
        topic = self.get_object()
        
        return True
    
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

class ResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    success_url = '/sudo/'

    def test_func(self):
        resource = self.get_object()
        
        return True

class PuzzleDetailView(DetailView):
    model = Puzzle
    slug_field = 'title'

class PuzzleCreateView(LoginRequiredMixin, CreateView):
    model = Puzzle
    fields = ['title', 'question', 'answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PuzzleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Puzzle
    slug_field = 'title'
    fields = ['title', 'question', 'answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        puzzle = self.get_object()
        
        return True

class PuzzleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Puzzle
    slug_field = 'title'
    success_url = '/sudo/'

    def test_func(self):
        puzzle = self.get_object()
        
        return True
  
# ends here

def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    context = {
        'topics': TOPIC_MGR.get_topics(),
    }
    return render(request, 'bibliomath/explore.html', context)

def topic(request, title):
    #topic = request.GET.get('topic','')
    resources = Resource.objects.filter(topic=title)
    context = {
        'title': title,
        'resources': resources,
    }
    return render(request, 'bibliomath/topic.html', context)


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
            'error': 'faulty/duplicate resource'
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
    return JsonResponse(PUZZLE_MGR.get_all_puzzles(), safe=False)

def check_answer(request):
    p_title = request.GET.get('title', '')
    p_submitted_answer = request.GET.get('answer', '')
    answer = PUZZLE_MGR.get_answer(p_title)
    print(p_submitted_answer, answer)
    # for interviewers: only top Gs check if a sting is a float like this
    if all(x in [str(i) for i in list(range(0,10))] + ['.', '-'] for x in p_submitted_answer) and abs(float(p_submitted_answer) - float(answer)) < ERROR:        # TODO can allow for similar answers not char-by-char correctness
        return JsonResponse({"result": "True"}, safe=False)
    else:
        return JsonResponse({"result": "False"}, safe=False)


# new view for collection addition
def addResource(request, id, title):
    print(id)
    collection = Collection.objects.filter(user=request.user).first()

    r1 = Resource.objects.filter(id=id).first()

    print(collection)
    collection.resources.add(r1)
    collection.save()
    print(collection)
    return redirect('topic', title)
    