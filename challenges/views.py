from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.


desafios_fisicos = {
    "janeiro": "Fazer 50 abdominais por dia",
    "fevereiro": "Correr 5 km três vezes por semana",
    "março": "Realizar 20 flexões de braço todos os dias",
    "abril": "Fazer 30 minutos de alongamento diariamente",
    "maio": "Saltar corda por 15 minutos seguidos, três vezes por semana",
    "junho": "Realizar 100 agachamentos todos os dias",
    "julho": "Nadar 500 metros três vezes por semana",
    "agosto": "Fazer 30 minutos de yoga ou meditação diariamente",
    "setembro": "Realizar 50 burpees todos os dias",
    "outubro": "Praticar ciclismo por 1 hora três vezes por semana",
    "novembro": "Fazer 10 minutos de prancha todos os dias",
    "dezembro": "Realizar 3 séries de 10 flexões horizontais todos os dias"
}

months = list(desafios_fisicos.keys())

def index(request):
    list_items = ""
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    


def monthly_challenge(request, month):
    try:
        challenge_text = desafios_fisicos[month]
    except:
        return HttpResponse('Digite um mês válido!')
    return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    month -= 1
    try:
        forward_month = months[month]
    except:
        return HttpResponse("Digite um número válido!")
    return HttpResponseRedirect(forward_month)
