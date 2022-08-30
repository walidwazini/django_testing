from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# * This is library, consist of key : value
monthly_target = {
    'jan': 'Eat more meat for entire month.',
    'feb': 'Do sunning for atleast 2 hours daily.',
    'mar': 'Drinks more plain water.',
    'apr': 'Eat more fish.',
    'may': 'Eat more meat for entire month.',
    'jun': 'Do sunning for atleast 2 hours daily.',
    'jul': 'Drinks more plain water.',
    'aug': 'Eat more fish.',
    'sep': 'Eat more meat for entire month.',
    'oct': 'Do sunning for atleast 2 hours daily.',
    'nov': 'Exercise 30minutes daily.',
    'dec': 'Read more books.'
}


def monthly_challenge_by_number(req, month):
    months = list(monthly_target.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid value for month.')

    # month is used as index
    redirect_month = months[month - 1]
    redirect_path = reverse('abc', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(req, month):
    try:
        challenge_text = monthly_target[month]
    except:
        return HttpResponseNotFound('The value not availble.')
    return HttpResponse(challenge_text)
