from django.urls import path
from.import views
urlpatterns = [
     path('userindex/',views.userindex,name='userindex'),        
     path('userhome/',views.userhome,name='userhome'),  
     path('hbooking/',views.hbooking,name='hbooking'),  
     path('hotelsview',views.hotelsview,name='hotelsview'), 
     path('singleview/<int:sid>/',views.singleview,name='singleview'),  
     path('userfeedback/',views.userfeedback,name='userfeedback'),
     path('userlogin',views.userlogin,name='userlogin'),
     path('userlogout',views.userlogout,name='userlogout'),   

]