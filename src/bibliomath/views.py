import json
from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Resource, Topic, Puzzle
from bibliomath.managers.topic_manager import TopicsManager
from bibliomath.managers.resource_manager import ResourceManager
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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

@login_required
def topic(request, title):
    resources_in = []
    resources_out = []
    collection_ids = []

    collection_res = Collection.objects.filter(user=request.user).values('resources')
    for res in collection_res:
        collection_ids.append(res['resources'])

    topic_res = Resource.objects.filter(topic=title).values('id')

    for res in topic_res:
        if res['id'] in collection_ids:
            resources_in.extend(Resource.objects.filter(id=res['id']))
        else:
            resources_out.extend(Resource.objects.filter(id=res['id']))

    context = {
        'title': title,
        'resources_in': resources_in,
        'resources_out': resources_out,
    }
    return render(request, 'bibliomath/topic.html', context)


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
    collection = Collection.objects.filter(user=request.user).first()

    r1 = Resource.objects.filter(id=id).first()

    collection.resources.add(r1)
    collection.save()
    return redirect('topic', title)
    