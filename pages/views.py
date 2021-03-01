from django.shortcuts import render
from django.http import HttpResponse
import requests,json
# Create your views here.

def index(request):
    #last value of moneys taken
    dolar=float(dolarValue())
    euro=float(euroValue())
    pound=float(gbpValue())
    aud=float(audValue())
    cad=float(cadValue())
    chf=float(chfValue())
    cny=float(cnyValue())
    rub=float(rubValue())
    sek=float(sekValue())

    #entered money value and selection is taken
    select=request.POST.get('moneys')
    inputMoneyValue=request.POST.get('money')
    moneyBack=0
    
    if inputMoneyValue is not "":
        if select=='usd':
            moneyBack=int(inputMoneyValue)*dolar
        elif select=='euro':
            moneyBack=int(inputMoneyValue)*euro
        elif select=='gbp':
            moneyBack=int(inputMoneyValue)*pound
        elif select=='aud':
            moneyBack=int(inputMoneyValue)*aud
        elif select=='cad':
            moneyBack=int(inputMoneyValue)*cad
        elif select=='chf':
            moneyBack=int(inputMoneyValue)*chf
        elif select=='cny':
            moneyBack=int(inputMoneyValue)*cny
        elif select=='rub':
            moneyBack=int(inputMoneyValue)*rub
        elif select=='sek':
            moneyBack=int(inputMoneyValue)*sek
    else: 
        moneyBack
        
    
    context={
        'dolarValue':dolar,
        'euroValue':euro,
        'gbpValue':pound,
        'audValue':aud,
        'cadValue':cad,
        'chfValue':chf,
        'cnyValue':cny,
        'rubValue':rub,
        'sekValue':sek,

        'moneyback':moneyBack,
        'select':select,
        
    
    }

    return render(request,'pages/index.html',context)

def dolarValue():
    result=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,5) #it make 5 digit number after dot
    return result

def euroValue():
    result=requests.get('https://api.exchangeratesapi.io/latest?base=EUR')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)#it make 4 digit number after dot
    return result

def gbpValue():
    #great
    result=requests.get('https://api.exchangeratesapi.io/latest?base=GBP')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def audValue():
    #australian dollar 
    result=requests.get('https://api.exchangeratesapi.io/latest?base=AUD')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def cadValue():
    #canada dollar
    result=requests.get('https://api.exchangeratesapi.io/latest?base=CAD')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def chfValue():
    #swiss frank
    result=requests.get('https://api.exchangeratesapi.io/latest?base=CHF')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def cnyValue():
    #chinese yuan
    result=requests.get('https://api.exchangeratesapi.io/latest?base=CNY')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def rubValue():
    #russian rouble
    result=requests.get('https://api.exchangeratesapi.io/latest?base=RUB')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result

def sekValue():
    #swedish krona
    result=requests.get('https://api.exchangeratesapi.io/latest?base=SEK')
    result=json.loads(result.text)
    result=result["rates"]["TRY"]
    result=round(result,4)
    return result