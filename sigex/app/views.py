"""
Definition of views.
"""

from app.models import Company, UserCompany
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from os import path
from django.core import serializers
from app.decorator import login_required_json

import json


def index(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title': 'Inicio',
            'message': 'Sigex ERP',
            'year': datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        })
    )

@login_required_json
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        })
    )

@login_required
def activecompany(request):
    """Renders the conpany page."""
    assert isinstance(request, HttpRequest)

    current_user = request.user
    companies = UserCompany.objects.filter(user = current_user)
    
    if request.method == 'POST':
        companyid = int(request.POST.get("activecompany"))
        companyname = ""
        isfound = False
        for company in companies: 
            if companyid == company.company.id:
                isfound = True
                companyname = company.company.CompanyName
        
        if isfound:
            request.session['activecompany_id'] = companyid
            request.session['activecompany_name'] = companyname
            return HttpResponseRedirect(reverse('home',))

    return render(
        request,
        'app/setcompany.html',
        context_instance = RequestContext(request,
        {
            'title': 'Compania Activa',
            'message': 'Selecction la compania activa',
            'companies': companies,
            'year': datetime.now().year,
        })
    )

@login_required
def seed(request):
    """Seeds the database with sample polls."""
    samples_path = path.join(path.dirname(__file__), 'samples.json')
    with open(samples_path, 'r') as samples_file:
        samples_polls = json.load(samples_file)

    for sample_poll in samples_polls:
        poll = Poll()
        poll.text = sample_poll['text']
        poll.pub_date = timezone.now()
        poll.save()

        for sample_choice in sample_poll['choices']:
            choice = Choice()
            choice.poll = poll
            choice.text = sample_choice
            choice.votes = 0
            choice.save()

    return HttpResponseRedirect(reverse('app:home'))
