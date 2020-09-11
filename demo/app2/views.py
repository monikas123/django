'''import a all'''
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import employee

# Create your views here.



def signup(request):
    '''
    add the user form
    :param username, firstname, lastn
    '''

    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        password = request.POST['password']
        signup = User.objects.create_user(username=username,
                                     first_name=first_name,
                                     last_name=last_name,
                                     email=email_id,
                                     password=password)
        signup.save()
        print("user create")
        return redirect('../')
    else:
        return render(request,'signup.html')

def user(request):
    if request.method == 'POST':
        if not 'id' in request.POST:
            name = request.POST.get('name')
            address = request.POST.get('address')
            salary = request.POST.get('salary')
            status = request.POST.get('status')
            user_info = employee(name=name, address=address, salary=salary, status=status)
            user_info.save()
            emp = employee.objects.all()
            return render(request, 'user_list.html', {'users': emp})
        else:
            obj  = employee.objects.get(id=request.POST['id'])
            obj.name = request.POST.get('name')
            obj.address = request.POST.get('address')
            obj.salary = request.POST.get('salary')
            obj.status = request.POST.get('status')
            obj.save()
            emp = employee.objects.all()
            return render(request, 'user_list.html', {'users': emp})

    else:
        return render(request, 'user.html')

def userList(request):
    allemployee = employee.objects.all()
    return render(request, 'user_list.html', {'users': allemployee})

def delete(request, id):
    emp = employee.objects.get(id = id)
    emp.delete()
    return redirect("/app2/userList")

def update(request, id):
    print(request.POST)
    emplu = employee.objects.get(pk  = id)
    # emplu.name = request.POST.get('name')
    # emplu.address = request.POST.get('address')
    # emplu.salary = request.POST.get('salary')
    # emplu.status = request.POST.get('status')
    # emplu.save()
    return render(request, 'edit.html', {'employe': emplu} )

def sendSimpleEmail():
    res = send_mail('Subject here',
                    'Here is the message.',
                    'singh.moni0596@gmail.com',
                    ['singh.moni0596@gmail.com'],
                    fail_silently=False,)
    return HttpResponse('%s'%res)
