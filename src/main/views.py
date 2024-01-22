from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

def home(request):
    return render(request, 'home.html')

def main(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbols'):
        char.extend(list('+-*/!@#$%&'))
    
    length = int(request.GET.get('length', 10))
    password = ""
    for x in range(length):      #start from 0 (want 16 digit random password)
        password +=random.choice(char)  #random char add gardai ja 16 digit navaye samma
    return render(request, 'password.html',{'password':password})

   # pas = {'password':password}
    
  #  return JsonResponse(pas)     pas vanni lai Json form ma pass garde

    


