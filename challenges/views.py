from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def monthly_challenge(request, month):
    if month == 'january':
        challenge_text = 'Vai correr meu caro!'
    else:
        challenge_text = 'Eu confio que você digitou um mês'
    return HttpResponse(challenge_text)
