from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import myform
from .forms import *
# Create your views here.
def display(request):
    return HttpResponse("<h3>Welcome to bix IT acc</h3>")

def myformview(request):
    if request.method == 'POST':
        a = request.POST['yourname']
        b = request.POST['contact']
        c = request.POST['email id']
        print(a, b, c)
        myform.objects.create(name=a, mobilenumber=b, email=c)
        return HttpResponse('Data created')
    return render(request, 'index.html', {})



def formclassview(request):

    if request.method=='POST':
        record = formclass(request.POST)
        if record.is_valid():
            record.save()
            return HttpResponseRedirect('/tables/')
    myforms = formclass()
    return render(request, 'index01.html', {'form':myforms})

def tablesview(request):
    result = myform.objects.all()
    return render(request, 'tables.html', {'record': result})

def search(request):
    if request.method == 'POST':
        search = request.POST['searchinput']
        result = myform.objects.filter(name=search)
        print(result)
        return render(request, 'tables.html', {'record': result})
    return render(request, 'search.html', {})


def update(request):
    urecord = myform.objects.get(name='gladwin')
    if request.method =='POST':
        record = formclass(request.POST, instance=urecord)
        if record.is_valid():
            record.save()
            return HttpResponseRedirect('/tables/')
    myforms = formclass(instance=urecord)
    return render(request, 'index01.html', {'form':myforms})

def deleterecord(request):
    drecord = myform.objects.filter(name='sivaraman')
    if drecord:
        drecord.delete()
        return HttpResponse('record deleted ')


