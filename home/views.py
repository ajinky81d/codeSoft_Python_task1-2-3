from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import requests


# Create your views here.
def home(request):
     return render(request,'home.html')

def index(request):
        #task=request.POST.get()
        if request.method=='POST':
          
          if 'name' in request.POST:
            name=request.POST.get('name') 
            contact=Contact(name=name,date=datetime.today())
            contact.save()
            messages.success(request,"Your Task is submited")
           
               
        tasks=Contact.objects.all()  
        context={'tasks':tasks}  
        return render(request,'index.html',context)

def delete(request,pk):
    item=Contact.objects.get(id=pk)
    
    if request.method=='POST':
        item.delete()
        return redirect('/todo')
    context={'item':item}
    return render(request,'del.html',context)
 
    

 

 
 
import json
def weather(request):
    if request.method=='POST':
        city=request.POST['city']
        if city == '':
              city="New York"
              BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
              API_KEY="2c65b4f3ee249a12d005320aa1c73c28"
    
              url=str(BASE_URL + "appid=" + API_KEY +"&q=" + city)
              response=requests.get(url).json()
              Humadity=response['main']['humidity']
              Temp=round(int(response['main']['temp'])-273.15,2)
              desc=response['weather'][0]['description']
              weather={'city':city,'desc':desc,'Temp':Temp,'Humadity':Humadity}
        else:

           BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
           API_KEY="2c65b4f3ee249a12d005320aa1c73c28"
    
           url=str(BASE_URL + "appid=" + API_KEY +"&q=" + city)
           response=requests.get(url).json()
           Humadity=response['main']['humidity']
           Temp=round(int(response['main']['temp'])-273.15,2)
           desc=response['weather'][0]['description']
           weather={'city':city,'desc':desc,'Temp':Temp,'Humadity':Humadity}
    else:
        city='Enter city'
        Humadity='In '
        Temp='In '
        desc= ''
        
    weather={'city':city,'desc':desc,'Temp':Temp,'Humadity':Humadity}    
    return render(request,'weather.html',weather)

     

     

def calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = Addition(num1,num2)
            return render(request,'calculator.html',{'result':result})
        
        if 'sub' in request.POST:
            result = Subtract(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
        if 'div' in request.POST:
            result = Divide(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
        if 'mul' in request.POST:
            result = Multiply(num1,num2)
            return render(request,'calculator.html',{'result':result})
    return render(request,'calculator.html')

def Addition(num1,num2):
    result = int(num1) + int(num2)
    return f"{num1}+{num2}={result}"
 
def Subtract(num1,num2):
    result = int(num1) - int(num2)
    return f"{num1}-{num2}={result}"
 
def Divide(num1,num2):
    result = int(num1) / int(num2)
    return  f"{num1}/{num2}={result}"
 
def Multiply(num1,num2):
    result = int(num1) * int(num2)
    return  f"{num1}*{num2}={result}"
