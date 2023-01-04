from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from.models import Phonebook
from . import form
from .form import ContactForm

# Create your views here.

def index(request):
    list = Phonebook.objects.all()
    data = {}
    data['phonebook'] = list
    return render(request, 'index.html', data)




def addcontact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        contactnum=request.POST.get('contactnum')
        index=Phonebook(name=name,contactnum=contactnum)
        if Phonebook.objects.filter(name = request.POST['name']).exists():
            return HttpResponse("this name is already existing")
        else:
            index.save()
            return render(request,"index.html")
    else:
        return render(request,"addcontact.html")

def search(request):
    search_input= request.GET.get('search')
    if search_input:
        phonebook=Phonebook.objects.filter(name=search_input)
    return render(request,'index.html',{'phonebook':phonebook})




def updatecontact(request, pk):
    task = Phonebook.objects.get(pk=pk)
    form = ContactForm(instance=task)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "updatecontact.html", {"task_edit_form": form})


def delete(request, pk):
    list= get_object_or_404(Phonebook, pk=pk)    
    if request.method=='POST':
        list.delete()
        return redirect('/')
    return render(request, 'delete.html',{'object':list})


