# Create your views here.
from django.http import HttpResponse

def index(request):
    #elec = Electricity(ActivityType.ELECTRICITY, ElectricityUnit.KILOWATT_HOUR, 100.5, "Germany", "Bavaria")
    return HttpResponse("test")

