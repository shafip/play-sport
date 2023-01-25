from django.shortcuts import render,redirect
from .forms import ProductForm,Register
from .models import Productmodel
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def booking(request):
    fom=ProductForm()
    dict_form = {
        'personal': Productmodel.objects.all()
    }
    return render(request,'booking.html',dict_form)

def formview(request):
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect,'checkout.html')
    else:
        form1=Register()
        dict={
            'form':form1
        }
        return render(request,'form.html',dict)


def checkout(request):
    if request.user.is_authenticated:
        order,created=Productmodel.objects.get_or_create()
        items=order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'bookdetails.html', context)

