from django.shortcuts import render
from .models import *
from .seralizer import taraz_ser
from rest_framework import generics
from django.http import HttpResponse
import json

def home_page(request):
    # Если запрос является POST-запросом
    if request.method == 'POST':
        danni = request.POST.get('name_sea')  # Получение данных из поля 'name_sea' в форме
        
        if 'канша озен бар' in danni:
            danni2 = taraz.objects.all().count()  
            return HttpResponse(f"{danni2} озен бар")
        elif 'озендер аттары' in danni:
            danni2 = taraz.objects.all().values_list('name_sea', flat=True)  # Получение списка имен из базы данных
            names = ', '.join(danni2)  
            return HttpResponse(names)
        elif 'озендер узындыгы' in danni:
            name_and_size = taraz.objects.all().values_list('name_sea', 'size_sez')
            return HttpResponse(name_and_size)

    else:
        context = taraz.objects.all() 
        return render(request, 'home.html', {'ozender': context})  

class tarazListView(generics.ListCreateAPIView):
    queryset = taraz.objects.all()
    serializer_class = taraz_ser

