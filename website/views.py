from django.template import loader
from django.http import HttpResponse


def main(request):
    context = {
        "title": "Main Page",
    }
    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))
