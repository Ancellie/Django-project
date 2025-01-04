from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 30 minutes every day.",
    "march": "Dedicate at least 20 minutes every day to learning Django!",
    "april": "Spend 20 minutes a day improving your Python skills.",
    "may": "Code for at least 20 minutes each day to sharpen your programming skills!",
    "june": "Practice coding for at least 20 minutes daily.",
    "july": "Focus on coding for 20 minutes every day to enhance your skills.",
    "august": "Set aside 20 minutes each day to learn coding techniques.",
    "september": "Commit to coding for 20 minutes a day to boost your knowledge.",
    "october": "Learn coding for 20 minutes every day to stay consistent.",
    "november": "Spend 20 minutes a day coding to continue your programming journey.",
    "december": "Dedicate 20 minutes a day to coding, even during the holidays!"
}


# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Page not found</h1>")
    redirect_month = months[int(month)-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>Page not found</h1>")
