from django.shortcuts import render

tasks = ["Alguma coisa", "Outra coisa", "Alguma outra coisa"]

# Create your views here.
def index(request):
  return render(request, "tasks/index.html", {
    "tasks": tasks
  })

def add(request):
  return render(request, "tasks/add.html")
