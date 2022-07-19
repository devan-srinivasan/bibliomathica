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