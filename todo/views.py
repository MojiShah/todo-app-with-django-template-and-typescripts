from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Todo
from .forms import TodoForm

# Create your views here.

class TodoListView(ListView):
    model = Todo;
    template_name = 'todo/todo_list.html';
    context_object_name = 'todos';
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context["completed_count"]=self.object_list.filter(is_done=True).count();
        return context
    
    
class TodoCreateView(CreateView):
    model = Todo;
    form_class = TodoForm;
    template_name = "todo/todo_form.html";
    success_url = reverse_lazy("todo-list");
    
class TodoDetailView(DetailView):
    model = Todo;
    template_name = "todo/todo_detail.html";
    context_object_name = "todo";
    
class TodoUpdateView(UpdateView):
    model=Todo;
    form_class = TodoForm;
    template_name = "todo/todo_form.html";
    success_url = reverse_lazy("todo-list");
    
class TodoDeleteView(DeleteView):
    model = Todo;
    template_name = "todo/todo_confirm_delete.html";
    success_url = reverse_lazy("todo-list");


