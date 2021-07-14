# Importamos o forms (para lidarmos com formulários)
from django import forms
# Para redirecionarmos o usuário para uma rota específica
from django.http import HttpResponseRedirect
# Para renderizar um HTML
from django.shortcuts import render
# reverse() nos retorna uma parte da URL especificada
from django.urls import reverse

# Definimos uma nova classe para criação de formulário
# Neste caso, essa classe permite criarmos um formulário com o input 'task' do tipo 'text
class NewTaskForm(forms.Form):
  task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
  # Verificamos se dentro da sessão particular temos a propriedade "tasks" (lembre-se que a session é como um grande dicionário)
  if "tasks" not in request.session:
    # Caso não exista, nós criamos a propriedade como uma lista vazia
    request.session["tasks"] = []

  return render(request, "tasks/index.html", {
    "tasks": request.session["tasks"]
  })

def add(request):
  # Verificando se o método de solicitação é POST (se o usuário enviou alguns dados do formulário)
  if request.method == "POST":
    # Pegamos todos os dados que foram enviados através do POST e salvamos dentro de 'form'
    form = NewTaskForm(request.POST)
    # Verificamos se todos os dados foram fornecidos no formato correto
    if form.is_valid():
      # Pegamos a tarefa que foi especificada no formulário e colocamos à lista de tarefas 'tasks'
      task = form.cleaned_data["task"]
      request.session["tasks"] += [task]

      # Redirecionamos o usuário para a rota definida com o nome de 'index' de nossa aplicação 'tasks' (no arquivo urls.py)
      # reverse() nos retorna a parte da URL especificada, neste caso, '/tasks'
      return HttpResponseRedirect(reverse("tasks:index"))
    else:
      # Renderizamos o mesmo arquivo add.html, mas com o mesmo formulário que foi preenchido. 
      # Assim, é possível visualizar todos os erros cometidos no preenchimento
      return render(request, "tasks/add.html", {
        "form": form
      })
  # Caso o método seja GET, significa que o usuário apenas tentou obter a página em vez de enviar dados a ela. 
  # Assim, enviamos apenas um formulário vazio
  return render(request, "tasks/add.html", {
    "form": NewTaskForm()
  })