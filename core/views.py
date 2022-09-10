from django.shortcuts import render
from matplotlib.style import context 
from core.forms import Contact_form
# Create your views here.
def home(request):
    context ={'home' : 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context ={'contact' : 'active'}
    return render(request, 'core/contact.html',context)

def data(request):
    if request.method == "POST":
        form=Contact_form(request.POST)
        fr=Contact_form()
        if form.is_valid():
            form.save()
            context ={'contact' : 'active'}
            return render(request,"core/contact.html",{"form":fr,'contact' : 'active'})
    else:
        form =Contact_form()
        context ={'contact' : 'active'}
        return render (request,"core/contact.html",{"form":form,'contact' : 'active'})