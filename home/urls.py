from django.urls import path
from .views import home,about, contact
#creating a urls file for our app then mapping and calling out our functions
urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact)
]