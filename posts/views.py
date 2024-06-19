from django.shortcuts import render
import json
import requests
from .models import Post
# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})

def weather(request):
    if request.method=='POST':
        city=request.POST.get('city')
        api_key = '11777f7e5db525a2012307e8c92b325f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = requests.get(url)
        json_data=res.json()
        data={
            "country_code": json_data['sys']['country'],
            "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
            "temp": f"{json_data['main']['temp']}K",
            "pressure": json_data['main']['pressure'],
            "humidity": json_data['main']['humidity'],
        }
    else:
        data={}
        # city='dsdsd'
    return render(request,'weather.html',{'data':data})