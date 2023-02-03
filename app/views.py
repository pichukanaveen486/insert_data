from django.shortcuts import render
from django.http import HttpResponse
from app.models import *



def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insertion is successfull')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ul=request.POST['ul']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ul)[0]
        W.save()
        return HttpResponse('webpage is created')

    return render(request,'insert_webpage.html',d)
