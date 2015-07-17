from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect

class SetCompanyMiddleware(object):
    """
    force go views only if there is an active company 
    """
    def process_request(self, request):
        return None

def setcompany(func):
    """
    A decorator, that can be used to authenticate some requests at the site.
    """
    if (not request.session.has_key('activecompany_id') or not request.session['activecompany_id']):
        return HttpResponseRedirect('/setcompany')
    else:
        return None


def _setcompany_helper(request):
    "This is the part that does all of the work"
    if (not request.session.has_key('activecompany_id') or not request.session['activecompany_id']):
        return HttpResponseRedirect('/setcompany')
    else:
        return None
