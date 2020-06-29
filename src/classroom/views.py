from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


@login_required
def index(request):
    return render(request, "classroom/index.html")


def assignmentPage(request, code):
    subject = Subject.objects.get(code=code)
    assignments = subject.assignment.all()
    data = {"assignments": assignments}
    print(data)
    return render(request, "classroom/assignment_page.html", data)
