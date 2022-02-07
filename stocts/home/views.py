

# Create your views here.
from django.shortcuts import render
import datetime
import re
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
#DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request,*args,**kwargs):
    return render(request, 'root.html')
#def home(request):
  #  return render(request, 'base.html')
def ageCalculator(request,*args,**kwargs):
    context = {
    'k1': 'Welcome to the Second page',
    
    }

    return render(request, 'inner-page.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request, 'inner-page.html',{})

def resume(request,*args,**kwargs):
    return render(request, 'resume.html')


 
def add(request,*args,**kwargs):
    

    val1=int( request.POST['num1'])
    val2= int(request.POST['num2'])
    val3=int( request.POST['num3'])
    val4= int(request.POST['num4'])
    val5=int( request.POST['num5'])
    val6= int(request.POST['num6'])
    
    
          
        # if birth date is greater then given birth_month  
        # then donot count this month and add 30 to the date so  
        # as to subtract the date and get the remaining days  
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 


          
    if (val1 > val4): 
            val5 = val5 - 1
            val4 = val4 + month[val2-1]  
                      
                      
        # if birth month exceeds given month, then  
        # donot count this year and add 12 to the  
        # month so that we can subtract and find out  
        # the difference  
    if (val2 > val5): 
             val6 = val6 - 1
             val2 = val2 + 12
                      
        # calculate day, month, year  
    calculated_day = val4 - val1  
    calculated_month = val5 - val2  
    calculated_year = val6 - val3 
  
        # calculated day, month, year write back 
        # to the respective entry boxes 
  
        # insert method inserting the   
        # value in the text entry box. 
          

    return render(request, 'resul.html',{'result1':calculated_day,'result2':calculated_month,'result3':calculated_year})




def contact(request,*args,**kwargs):
    return render(request, 'calc.html')

def service(request,*args,**kwargs):
    return render(request, 'service.html')

def hom(request,*args,**kwargs):
    
    if request.method== 'POST':
        message=request.POST['message']
        name=request.POST['name']
        subject=request.POST['subject']
        message_email=request.POST['email']
        send_mail(subject, 
        name,
          message,
         
          message_email, 
          recipient_list=['oyedotuna@gmail.com'], 
          fail_silently=False, 
          auth_user=None, 
          auth_password=None, 
          connection=None, 
          html_message=None)
        return render(request, 'inner-page.html',{'message':message})
    else:
        return render(request, 'inner-page.html',{})


   