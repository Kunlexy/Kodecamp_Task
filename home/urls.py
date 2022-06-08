from django.urls import path
from .views import home,about, contact
#creating a urls file for our app then mapping and calling out our functions

app_name = "home"

urlpatterns = [
    path('', home, name="homeview"),
    path('about/', about, name="aboutview"),
    path('contact/', contact, name="contactview")
]