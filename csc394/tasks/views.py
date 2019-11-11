from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.models import User

# Create your views here.

def taskView (request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'tasks/index.html',
    {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'], title = request.POST['title'], date= request.POST['date'])
    new_item.save()
    return HttpResponseRedirect('/tasks/')

    
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks/')
<<<<<<< HEAD

# def profile(request):
#     args = {'user': request.user.pk}
#     return render(request, 'tasks.html', args)

def testTaskView(request):
    return render(request, 'testing.html')
    #create new todo all_items

<<<<<<< HEAD
def details (request, todo_id):
    return HttpResponse("<h2>Details for Task: {0} </h2>".format(todo_id))
>>>>>>> 737476c08d98195d3cc6f45774aa5ad4e23a7e51
=======
def todoDetails(request, todo_id):
    return render(request, 'tasks/taskDetails.html', {'todo_id': todo_id})
>>>>>>> 9b20a630df28442b4cfb3d09350b7073256bc216
