from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf




def log_in(request):
    results = {}
    results.update(csrf(request))
    return render_to_response("log_in.html", results)

def authenticate(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = auth.authenticate(username=username, password=password)

    redirect = HttpResponseRedirect("/accounts/invalid_log_in")
    if user is not None:
        auth.login(request, user)
        redirect = HttpResponseRedirect("/accounts/logged_in")

    return redirect


def logged_in(request):
    return render_to_response("logged_in.html", {"first_name": request.user.first_name})

def log_out(request):
    auth.logout(request)
    return render_to_response("logged_out.html")

def invalid_log_in(request):
    return render_to_response("invalid_log_in.html")