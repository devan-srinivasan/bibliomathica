from django.shortcuts import render

# Create your views here.
def explore(request):
    # make some request to MongoDB
    # get data and format it accordingly to display
    topics = [
        {  
            'title': 'Geometry', 
            'description': 'Everything to do with shapes',
            'link': 'https://youtube.com',
        }
    ] * 5
    context = {
        'topics': topics
    }
    return render(request, 'bibliomath/explore.html', context)