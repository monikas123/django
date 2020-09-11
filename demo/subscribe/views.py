from django.shortcuts import render
from demo.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Monika'
        message = 'Testing Mails'
        recepient = str(sub['Email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})


def cripsy(request):
    formq = forms.PersonalDataForm()
    return render(request, 'subscribe/crispy_form.html',{'emp':formq })

def exapleForm(request):
    exp = forms.ExampleForm()
    return render (request, 'demo.html', {'exp': exp})

def addressform(request):
    add = forms.AddressForm()
    return render (request, 'addressform.html', {'address': add})