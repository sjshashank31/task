from django.shortcuts import render

# Create your views here.


def getTasks(request):
    return render(request, 'tasks.html')