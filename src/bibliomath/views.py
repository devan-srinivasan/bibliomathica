from django.shortcuts import render

# Create your views here.
def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    context = {}
    return render(request, 'bibliomath/explore.html', context)