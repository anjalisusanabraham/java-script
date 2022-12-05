from django.shortcuts import render

def js_largest(request):
    return render(request,'js/largest.html')

def js_secondlargest(request):
    return render(request,'js/secondlargest.html')

def js_noofelements(request):
    return render(request,'js/noofelements.html')

def js_palindrom(request):
    return render(request,'js/palindrom.html')

def js_search(request):
    return render(request,'js/search.html')
# Create your views here.
