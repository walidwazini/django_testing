from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'nov': 'Exercise 30 minutes daily.',
    'dec': 'Read more books.'
}

month_longname = {
    'jan': 'January',
    'feb': 'February',
    'mar': 'March',
    'apr': 'April',
    'may': 'May',
    'jun': 'June',
    'jul': 'July',
    'aug': 'August',
    'sep': 'September',
    'oct': 'October',
    'nov': 'November',
    'dec': 'December'
}


def index(req):
    list_items = ''
    months = list(monthly_target.keys())

    # for month in months:
    #     capitalizedMonth = month.capitalize()
    #     month_path = reverse('abc', args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalizedMonth}<a/><li/>'
    # response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)
    return render(req,'challenges/index.html',{
        'months': months,
    })


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
        # selected_month = month.capitalize()
        selected_month = month_longname[month]

        print(selected_month)
        
        # Make it dynamic 
        return render(req,'challenges/challenge.html', {
            "text": challenge_text,
            "month" : selected_month,
        })

    except:
        return HttpResponseNotFound('The value not availble.')
