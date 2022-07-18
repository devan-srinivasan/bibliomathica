from django.shortcuts import render

# Create your views here.
def explore(request):
    context = {}
    return render(request, 'bibliomath/explore.html', context)