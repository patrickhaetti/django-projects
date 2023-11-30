from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Januar hallo"
        
    elif month == "february":
        challenge_text = "feb hallo"
        
    else:
        return HttpResponseNotFound("Not supported")
        
    return HttpResponse(challenge_text)