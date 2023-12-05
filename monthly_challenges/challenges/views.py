from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "january stuff",
    "february": "february stuff",
    "march": "march stuff"
}

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    actual_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[actual_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>Not supported</h1>")