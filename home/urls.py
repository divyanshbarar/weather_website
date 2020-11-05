
from django.contrib import admin
from django.urls import path,include
from home import views


#admin.site.site_header="My Portfolio"
#admin.site.site_title=" Welcome Divyansh"
#admin.site.index_title="This is Divyansh Portfolio"
urlpatterns = [
    path('',views.index, name='home'),
    path('delete/<city_name>/',views.delete_city, name='delete_city'),
    #path('contact',views.contact, name='contact')
]