from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView,View
from django.utils.decorators import method_decorator
from .forms import CommentForm, TaskForm,TaskEditForm
from main_app.models import Task,Comment
from django.db.models import Q     
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# @method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

# @login_required
# def About(request):
#     # template_name = "about.html"
#     return render(request,"about.html")

@login_required
def CreateTask(request):
    form = TaskForm()
    commentform = CommentForm()
    
    context = {}
    if request.method == 'POST' and 'addTask' in request.POST:
        form = TaskForm(request.POST)
        # form['user'] = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user  # Logic TO save for current user(logged)
            obj.save()
            return redirect('/addtask')
        
    if request.method == 'POST' and 'addComment' in request.POST:
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            obj = commentform.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/addtask')
    
    context["tasks"] = Task.objects.filter(user=request.user)
    context["header"] = "Dumbo! Add the Task before you forget"
    commentsQuery =  Comment.objects.filter(user = request.user) ### Need to revisit

    if commentsQuery:
        commentsQuery =  Comment.objects.get(user = request.user) ### Need to revisit
        context["comment"] = commentsQuery
    
    context['form']=form
    context['commentform']=commentform
    
    return render(request, 'create_task.html', context)


@login_required
def UpdateTask(request,pk):
    singletask = Task.objects.get(id=pk)
    form = TaskEditForm()
    if request.method == 'POST':
        form = TaskEditForm(request.POST,instance =singletask)
        # form['user'] = request.user
        if form.is_valid():
            form.save()
            return redirect('addtask')
    
    context = {'form':form}
    context['task'] = singletask
    return render(request,"update_task.html",context) 


@login_required
def DeleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
    return redirect('/addtask')
    
    # return render(request,"artist_delete.html") 
    

@login_required
def DeleteComment(request):
    comment = Comment.objects.filter(user = request.user)

    if request.method == 'POST':
        comment.delete()
    return redirect('/addtask')    

# @login_required
# def AddComment(request):
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         # form['user'] = request.user
#         if form.is_valid():
#             form.save()
#             return redirect('/addtask')
     
#     return redirect('/addtask')

@login_required
def SearchTask(request):
    taskTag = request.GET.get("task")
    # print("--",len(taskTag))
        # If a query exists we will filter by tasktag 
    context={}
    if taskTag != None:
        #Example 1-- django filter with AND 
        # context["tasks"] = Task.objects.filter(name__icontains=taskTag , user=request.user)
        
        # Example 2 with AND(&) operater
        context["tasks"] = Task.objects.filter(Q(name__contains = taskTag.casefold()) & Q(user=request.user))
        print(context)
    else:
         context["empty"] = "No Task Available"
    return render(request,"search_task.html",context)


def Signup(request):
    form = UserCreationForm()
    context = {"form": form}
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('/addtask')
    else:
        context = {"form": form}
        return render(request, "registration/signup.html", context)