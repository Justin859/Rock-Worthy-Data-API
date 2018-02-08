from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def test(request):

    response_data = {'name': 'Test Response Successful'}

    return JsonResponse(response_data)
