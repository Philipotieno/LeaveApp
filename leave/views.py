from django.shortcuts import redirect, render

from leave.forms import LeaveForm
from leave.models import Leave

# Create your views here.


def show(request):
    leaves = Leave.objects.all()
    return render(request, "show.html", {"leaves": leaves})


def request_leave(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            # try:
            form.save()
            return redirect("/")
            # except:
            #     pass
    else:
        form = LeaveForm()
    return render(request, "index.html", {"form": form})


def edit(request, id):
    leave = Leave.objects.get(id=id)
    return render(request, "edit.html", {"leave": leave})


def update(request, id):
    leave = Leave.objects.get(id=id)
    form = LeaveForm(request.POST or None, instance=leave)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "edit.html", {"leave": leave})
