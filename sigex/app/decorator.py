from django.contrib.auth.decorators import resolve_url
from django.http import HttpResponseRedirect, HttpResponse

def login_required_json(f):
    def inner(request, *args, **kwargs):
        #this check the session if userid key exist, if not it will redirect to login page
        if (not request.session.has_key('activecompany_id') or not request.session['activecompany_id']):
            return HttpResponseRedirect('/setcompany')
        else:
            return f(request, *args, **kwargs)
    return inner