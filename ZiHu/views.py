from django.shortcuts import render

# Create your views here.
def home(request):
    context ={}
    return render(request,'./ZiHu/home.html',context)


def archives(request):
    context ={}
    return render(request,'./ZiHu/archives.html',context)


def categories(request):
    context ={}
    return render(request,'./ZiHu/categories.html',context)


def tag(request):
    context ={}
    return  render(request,'./ZiHu/tag.html',context)

