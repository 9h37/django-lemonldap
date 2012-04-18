from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.models import User

def home (request):
    data = {
        "user": request.user,
        "is_logged_in": request.user.is_authenticated()
    }

    return render_to_response("test.html", data, context_instance=RequestContext(request))
