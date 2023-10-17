from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context["form"] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}

    context["dataset"] = StudentModel.objects.all()

    return render(request, "list_view.html", context)
