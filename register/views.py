from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Akun telah dibuat untuk {username}. Kamu bisa login sekarang.",
            )
            return redirect("user-login")
    else:
        form = UserCreationForm()

    context = {
        "title": "Register Page",
        "form": form,
    }
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context, request))
