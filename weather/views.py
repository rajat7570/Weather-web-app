from django.shortcuts import render, redirect
import requests
from .models import WH
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def list_w(request):
    weather = WH.objects.all().order_by('-added_date')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    for w in weather:
        r = requests.get(url.format(w.text)).json()
        city_weather = {'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                    }
        WH.objects.filter(text=w.text).update(temperature=city_weather['temperature'], descrip=city_weather['description'], icon=city_weather['icon'])

    return render(request, 'weather/index.html', {'weather': weather})

@csrf_exempt
def add_city(request):
    current_date = timezone.now()
    city = request.POST["content"]
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    r = requests.get(url.format(city)).json()

    city_weather= {'city': city,
            'temperature': r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
                  }
    print(city_weather)
    WH.objects.create(added_date=current_date, text=city_weather['city'], temperature=city_weather['temperature'], descrip=city_weather['description'], icon=city_weather['icon'])
    return redirect('list_w')

@csrf_exempt
def delete_city(request,pk):
    WH.objects.filter(id=pk).delete()
    return redirect('list_w')
