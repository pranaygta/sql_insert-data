from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def topic_name(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'topic_name.html',d)


def webpage(request):
    webpage=Webpage.objects.all()
    #webpage=Webpage.objects.exclude(topic_name='cricket')
    #webpage=Webpage.objects.order_by('-name')
    #webpage=Webpage.objects.filter(name__startswith='a')
    #webpage=Webpage.objects.filter(name__endswith='r')
    #webpage=Webpage.objects.filter(name__contains='h')
    #webpage=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}a')
    #webpage=Webpage.objects.filter(name__in=('Adam','Michele'))
    d={'ws':webpage}
    return render(request,'webpage.html',d)    

def access_records(request):
    a=AccessRecords.objects.all()
    #a=AccessRecords.objects.filter(date='1987-05-27')
    #a=AccessRecords.objects.filter(date__gt='1987-05-27')
    #a=AccessRecords.objects.filter(date__gte='1987-05-27')
    #a=AccessRecords.objects.filter(date__lt='2021-06-16')
    #a=AccessRecords.objects.filter(date__lte='2021-06-16')
    #a=AccessRecords.objects.filter(date__year='2021')
    #a=AccessRecords.objects.filter(date__day='27')
    #a=AccessRecords.objects.filter(date__month='9')
    d={'aa':a}
    print(a)
    return render(request,'AccessRecordss.html',d)    