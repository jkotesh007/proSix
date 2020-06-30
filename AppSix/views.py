from django.shortcuts import render
from django.http import HttpResponse
from AppSix.models import Topic,Webpage,AccessRecord

# Create your views here.
def request(response):
    return HttpResponse("You are looking")

def request2(response):
    return render(response,'AppSix/index.html')
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record': webpages_list}
    return render(request,'AppSix/index.html',context=date_dict)
