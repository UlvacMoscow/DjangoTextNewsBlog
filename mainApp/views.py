from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html',
    {'values' : ['Вопросы можете задать по телефону', '8-495-444-32-11', 'po4ta@mail.com']})
