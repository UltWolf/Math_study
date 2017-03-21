from django.shortcuts import render
from Tasks.models import MathTask
from Theory.models import MathTheory
def Tasks(request,Tasks_name_slug):
    context_dict = {}
    try:
     theory = MathTheory.objects.get(slug = Tasks_name_slug)

     context_dict['theo_name']= MathTheory.title
     context_dict['Tasks_name_slug']=Tasks_name_slug
     task = MathTask.objects.filter(Theor=theory)
     context_dict['task'] = task
     context_dict['theo'] = theory

    except MathTheory.DoesNotExist:
     pass
    return render(request, 'Tasks/tasks.html', context_dict)

def Task_all(request):
    context_dict = {}
    task = MathTask.objects.all()
    context_dict['task'] = task
    return render(request,'Tasks/task.html',context_dict )