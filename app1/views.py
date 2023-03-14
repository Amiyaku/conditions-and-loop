from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10, 'b':20}
    return render(request,'conditions.html',d)




def loop(request):
    d={'name':'AMIYA'}
    return render(request,'loop.html',d)
