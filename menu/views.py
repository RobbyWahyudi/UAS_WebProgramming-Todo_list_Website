from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    context = {
        "title": "To-do List Website",
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
