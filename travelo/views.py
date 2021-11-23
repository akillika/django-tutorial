from django.http import response
from django.shortcuts import render

from travelo.models import Destination

# Create your views here.
def index(request):

    # dests = Destination.objects.all()

    dests = Destination.objects.all()




    return render(request, 'index.html',{'dest1':dests})