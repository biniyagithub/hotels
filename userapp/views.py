from django.shortcuts import render,redirect
from userapp.models import *
from hoteladmin.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def userindex(request):
    return render(request,'userindex.html')

def userhome(request):
    return render(request,'user_home.html')

def hbooking(request):
    if request.method=="POST":
        name1 = request.POST.get('name')
        address1 = request.POST.get('address')
        image1 = request.FILES.get('image')
        place1 = request.POST.get('place')
        email1 = request.POST.get('email')
        password1 = request.POST.get('pass')
        date1 = request.POST.get('indate')
        date2 = request.POST.get('outdate')
        room1 = request.POST.get('rooms')
        data = Customer(cname=name1,caddress=address1,cimage=image1,cplace=place1,cemail=email1,cpassword=password1,checkindate=date1,checkoutdate=date2,rooms=room1)
        data.save()
    return render(request,'hotel_booking.html')

def hotelsview(request):
    if 'u_id' in request.session:
        hdata = Hotel.objects.all()
        return render(request,'hotels_view.html',{'hdata':hdata})
    return render(request,"customer_login.html",{'msg':"u r not login yet"})
    

def singleview(request,sid):
    sdata = Hotel.objects.filter(id=sid)
    return render(request,'single_hotel.html',{'sdata':sdata})

def userfeedback(request):
     if request.method=="POST":
         cusname = request.POST.get('name')
         cusemail = request.POST.get('email')
         msg = request.POST.get('message')
         data= Contacts (name=cusname,email=cusemail,message=msg,)
         data.save()
     return render(request,'feedback.html')


def userlogin(request):
    if request.method == "POST":
        useremail=request.POST.get('email')
        userpassword=request.POST.get('password')
        if Customer.objects.filter(cemail=useremail,cpassword=userpassword).exists():
           data = Customer.objects.filter(cemail=useremail,cpassword=userpassword).values('cname','cplace','caddress','id').first()
           request.session['name_u'] = data['cname']
           request.session['place_u'] = data['cplace'] 
           request.session['address_u'] = data['caddress']
           request.session['u_id'] = data['id']
           request.session['useremail_u'] = useremail
           request.session['password_u'] = userpassword
           return redirect('userhome') 
        else:
            return render(request,'user_login.html',{'msg':'invalid user credentials'})
    else:
        return render(request,'user_login.html')

def userlogout(request):
    del request.session['name_u']
    del request.session['place_u']
    del request.session['address_u']
    del request.session['u_id']
    del request.session['useremail_u']
    del request.session['password_u']
    return redirect('userlogin')

