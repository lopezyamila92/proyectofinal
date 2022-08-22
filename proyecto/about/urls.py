from django.urls import path 
from about.views import contact_us_view
from about.views import about

urlpatterns = [
    path('contact-us/', contact_us_view, name = 'contact-us'),
    path ('about/', about, name = 'about')
    

]