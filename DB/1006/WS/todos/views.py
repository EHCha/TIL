from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Todos
from .forms import TodosForm
# Create your views here.

@login_required
def index(request):
    todos = Todos.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodosForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)
