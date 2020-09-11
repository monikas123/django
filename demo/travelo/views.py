from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

     dest1 = Destination()
     dest1.name = 'Mumbai'
     dest1.image ='destination_1.jpg'
     dest1.price = 700
     dest1.desc = 'Nulla pretium tincidunt felis, nec.'
     dest1.offer = True

     dest2 = Destination()
     dest2.name = 'Hdrabaad'
     dest2.image ='destination_2.jpg'
     dest2.price = 650
     dest2.desc = 'Nulla pretium tincidunt felis, nec.'
     dest1.offer = False

     dest3 = Destination()
     dest3.name = 'Delhi'
     dest3.image ='destination_3.jpg'
     dest3.price = 750
     dest3.desc = 'Nulla pretium tincidunt felis, nec.'
     dest1.offer = True

     dests = [dest1,dest2,dest3]

     return render(request,'index.html', {'dests':dests})