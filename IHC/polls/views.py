from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, Choice

import folium as fl
from django.views.generic import TemplateView

# Class based view to render map
class FoliumView(TemplateView):
    template_name = 'polls/map_page.html'

    def get_context_data(self, **kwargs):
        # Creating Map instance
        flMap = fl.Map(location=[-16.737, -43.865],
                       )

        # Adding one marker to test
        fl.Marker(location=[-16.737, -43.865], popup='Testing').add_to(flMap)



        flMap = flMap._repr_html_()

        return {"map" : flMap}



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    RESPONSE = f'You are looking at the {question_id}#'
    return HttpResponse(RESPONSE)

def vote(request, question_id):
    RESPONSE = f'Voted on the {question_id}#!'
    return HttpResponse(RESPONSE)

def choices(request, question_id):
    # Question ID in db
    q = Question.objects.get(id=question_id)

    all_choices = q.choice_set.all()

    # Output text
    context = { 'choices': all_choices,
                'question': q
              }

    # template = loader.get_template('polls/index.html')

    return render(request, 'polls/index.html', context)



def map_show(request, **kwargs):
    #creation of map comes here + business logic
    m = fl.Map([51.5, -0.25], zoom_start=10)
    test = fl.Html('<b>Hello world</b>', script=True)
    popup = fl.Popup(test, max_width=2650)
    fl.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m=m._repr_html_() #updated
    context = {'map': m}

    return render(request, 'polls/map_page.html', context)
