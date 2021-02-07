from django.shortcuts import render

# Create your views here.


def jindex(request):
    return render(request, 'jindex.html')
