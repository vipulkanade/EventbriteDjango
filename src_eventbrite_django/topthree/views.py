from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime

from .forms import CategoriesForm
from .services import results

import os

# Home Template view which renders home.html
def home(request):
    form = CategoriesForm()

    context = {
                'title': "Event Search",
                'form': form,
    }

    return render(request, "home.html", context)


# This function will render the list of events that the user selected 3 categories from
def getEvents(request):
    page_id = 1
    auth_token = os.environ.get('AUTH_TOKEN')
    category_1 = None
    category_2 = None
    category_3 = None

    # Check for if method is POST request and isn't a ajax request
    if request.method == 'POST' and not request.is_ajax():
        form = CategoriesForm(request.POST)
        if form.is_valid():
            request.session['category_1'] = form.data['category_1']
            request.session['category_2'] = form.data['category_2']
            request.session['category_3'] = form.data['category_3']

        else:
            context = {
                'title': "Search Events",
                'form': form,
            }
            return render(request, 'home.html', context)

    # check ajax call for binding pagination to calling its corresponding eventbrite api
    elif request.is_ajax():
        data = request.POST
        page_id = data['page_id']

        category_1 = request.session['category_1']
        category_2 = request.session['category_2']
        category_3 = request.session['category_3']

        response, status_code = results(category_1, category_2, category_3,
            str(page_id), auth_token)

        events = response.json()['events']
        template = get_template('event_details.html')

        variables = Context({
            'events': events,
        })

        events_template = template.render(variables)
        return HttpResponse(events_template)

    elif request.method == 'GET':
        return redirect('/')

    category_1 = request.session['category_1']
    category_2 = request.session['category_2']
    category_3 = request.session['category_3']

    response, status_code = results(category_1, category_2, category_3,
        str(page_id), auth_token)

    events = response.json()['events']
    items = response.json()['pagination']['object_count']
    items_on_page = response.json()['pagination']['page_size']


    context = {
        'events': events,
        'title': "Search Results",
        'itemsOnPage': items_on_page,
        'items': items,
    }

    return render(request, "list_of_events.html", context)









