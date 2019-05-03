from django.shortcuts import render
from urlapp import models

# Create your views here.
def index(request):
    context_dict={'text':'Hello World','number':'100'}
    return render(request,'urlapp/index.html',context_dict)

def relative(request):
    return render(request,'urlapp/relative_url.html')

def other(request):
    return render(request,'urlapp/other.html')
