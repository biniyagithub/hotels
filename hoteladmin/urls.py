from django.urls import path
from.import views

urlpatterns = [
    path('adminindex/',views.adminindex,name='adminindex'),
    path('hotel/',views.hotel,name='hotel'),
    path('hotelview/',views.hotelview,name='hotelview'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('viewdetails/<int:hotelid>/',views.viewdetails,name='viewdetails'),
    path('home/',views.home,name='home'),
    path('viewbooking/',views.viewbooking,name='viewbooking'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
   


]