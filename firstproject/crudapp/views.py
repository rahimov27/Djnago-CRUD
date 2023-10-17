from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect


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

    context["dataset"] = StudentModel.objects.all().order_by("-id")

    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = StudentModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(StudentModel, id=id)

    form = StudentForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(StudentModel, id=id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
