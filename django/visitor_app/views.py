from django.shortcuts import render
from visitor_app.models import VisitFor,Department,Visitor,Visit
from visitor_app.forms import VisitForm
from django.http import HttpResponseRedirect

def visit_index(request):
    visit = Visit.objects.all()
    context = {
        'visit': visit
    }
    return render(request, 'visit_index.html', context)

def create_visit(request):

    form = VisitForm()
    if request.method == "POST":
        form = VisitForm(request.POST)

    context = {
    	'form':form
    }
    return render(request, "visit_create.html",context)

def save_visit(request):
    form = VisitForm()
    
    visitor = Visitor.objects.filter(pk=request.POST["name"])
    visitfor = VisitFor.objects.filter(pk=request.POST["visit_to"])
    department = Department.objects.filter(pk=request.POST["department"])
    # if not department:
    #     department = Department(
    #         department_name=request.POST["department"].department_name)
    #     department.save()
    # if not visitfor:
    #     visitfor = VisitForm(
    #         name=request.POST["visit_to"].vis,
    #         )
    #     visitfor.save()
    
    visit = Visit(
        visitor_name= visitor[0],
        visitor_email = request.POST["email"],
        visitor_phone = request.POST["phone"],
        visit_to = visitfor[0],
        department = department[0],
        purpose = request.POST["purpose"]
    )
    visit.save()
    latest_visit = Visit.objects.all()
    context = {
        'visit':latest_visit
    }
    return HttpResponseRedirect('http://localhost:8000/visitor_app/visit')
