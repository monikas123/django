'''import file in render '''
from django.shortcuts import render



# Create your views here.
def home(request):
    '''show the name for feild'''
    return render(request,'home.html', {'name':'Monika'})

def add(request):
    '''add two number in string'''
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1+val2
    res = val1+val2

    return render(request, 'result.html', {'result':res})
