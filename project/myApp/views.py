from django.shortcuts import render
from .models import info
from django.shortcuts import get_object_or_404

# Create your views here.
def Home(request):
    information = info.objects.all()
    return render(request,'index.html',{'information':information})

def detail_info(request,info_id):
    infor = get_object_or_404(info,pk=info_id)
    return render(request,'detail.html',{'infor':infor})