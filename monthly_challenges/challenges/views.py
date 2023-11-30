from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


monthly_challenges = {
    "january": "january stuff",
    "febuary": "february stuff",
    "march": "march stuff"
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not supported")