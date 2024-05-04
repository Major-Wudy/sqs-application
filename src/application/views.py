# Create your views here.
from django.http import HttpResponse

def index():
    return HttpResponse("test")

