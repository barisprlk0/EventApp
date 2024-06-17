from django.shortcuts import render
from travel.models import TravelModel
from django.utils import timezone

def index(request):
    now = timezone.now()
    last_24_hours = now - timezone.timedelta(hours=24)
    travels = TravelModel.objects.filter(c_date__gte=last_24_hours)
    
    return render(request, 'home/index.html', {'travels': travels})
