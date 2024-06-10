from django.shortcuts import render, redirect
from core.forms import TodoForm
from core.models import Todo

def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    print(form)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
     
    return render(request,'home.html',{'form':form, 'todos': todos})
