from django.shortcuts import render

# Create your views here.
def app1(request):
    return render(request, 'app1/all_app1.html')