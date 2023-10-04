from django.shortcuts import render,redirect
from hoteladmin.models import *
from userapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def adminindex(request):
    return render(request,'admin_idex.html')
    
def hotel(request):
    if request.method=="POST":
        name1 = request.POST.get('name')
        address1 = request.POST.get('address')
        image1 = request.FILES['image']
        description1 = request.POST.get('description')
        state1 = request.POST.get('state')
        city1 = request.POST.get('city')
        pin1 = request.POST.get('pin')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        price1 = request.POST.get('price')
        data = Hotel(hname=name1,haddress=address1,himage=image1,hdescription=description1,hstate=state1,hcity=city1,hpin=pin1,hemail=email1,hpassword=password1,hprice=price1)
        data.save()
    return render(request,'hotel_registration.html')
        
def hotelview(request):
    hdata = Hotel.objects.all()
    return render(request,'view_hotels.html',{'hdata':hdata})

def edit(request,id):
    edata=Hotel.objects.filter(id=id)
    return render(request,'edit.html',{'edata':edata})

def update(request,id):
    if request.method=="POST":
        name1 = request.POST.get('name')
        address1 = request.POST.get('address')
        description1 = request.POST.get('description')
        state1 = request.POST.get('state')
        city1 = request.POST.get('city')
        pin1 = request.POST.get('pin')
        price1 = request.POST.get('price')
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Hotel.objects.get(id=id).himage
            Hotel.objects.filter(id=id).update(hname=name1,haddress=address1,hdescription=description1,hstate=state1,hcity=city1,hpin=pin1,hprice=price1,himage=file)
        return redirect('hotelview')
    return redirect('hotelview')

def delete(request,id):
    Hotel.objects.filter(id=id).delete()
    return redirect('hotelview')

def viewdetails(request,hotelid):
    hoteldata = Hotel.objects.filter(id=hotelid)
    return render(request,'view1_hotel.html',{'hoteldata':hoteldata})

def home(request):
    return render(request,'admin_home.html')

def viewbooking(request):
    bdata = Customer.objects.all()
    return render(request,'view_bookings.html',{'bdata':bdata})

def viewfeedback(request):
    fdata = Contacts.objects.all()
    return render(request,'view_feedback.html',{'fdata':fdata})




