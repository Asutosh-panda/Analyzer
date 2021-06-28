
from django.shortcuts import render,HttpResponse
from .mlModel.imdb import imdbModel

# Create your views here.


def index(request):
    content={"content":""}
    if request.method == 'POST':
        print(request.POST.get('submit'))
        y_pred = imdbModel(str(request.POST.get('submit')))
        content={"content":y_pred}
    

    return render(request,'home.html',context=content)
