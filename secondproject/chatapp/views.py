from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import MessageForm
from .models import MessageModel


def create_view(request):
    context = {}

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context["form"] = form

    return render(request, "index.html", context)


def list_view(request):
    context = {}

    context["dataset"] = MessageModel.objects.all()

    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = MessageModel.objects.get(id=id)
    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(MessageModel, id=id)

    form = MessageForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/" + id)

    context["form"] = form

    return render(request, "update_view.html", context)
