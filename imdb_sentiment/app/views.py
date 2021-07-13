from django.shortcuts import render,HttpResponse
from .mlModel.imdb.imdb import imdbModel
from .mlModel.hate_speech.hate import hateModel
# Create your views here.

def home(request):
    return render(request,"home.html")

def imdb(request):
    content={"content":""}
    if request.method == 'POST':
        print(request.POST.get('submit'))
        y_pred = imdbModel(str(request.POST.get('submit')))
        content={"content":y_pred}
    return render(request,'imdb.html',context=content)


def hate(request):
    context = {'content':""}
    hateModel([""])
    if request.method=="POST":
        content = str(request.POST.get('hateSubmit'))
        content = hateModel([content])
        context ={'content':content}
    return render(request,'hate.html',context)