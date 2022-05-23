from django.shortcuts import render

# Create your views here.
#creating views using functions and rendering the html files in our templates folders
def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")