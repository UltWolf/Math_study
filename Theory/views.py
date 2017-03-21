from django.shortcuts import render
from Theory.models import MathTheory
def List_Theory(request):
    theory = MathTheory.objects.all()
    context_dict = {'theory':theory}
    return render(request,'Theory/theory.html',context_dict)

