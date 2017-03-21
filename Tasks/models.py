from django.db import models
from Theory.models import MathTheory
class MathTask(models.Model):
 Theor = models.ForeignKey(MathTheory,related_name='Теория')
 tasks = models.CharField(max_length=300)
 result = models.CharField(max_length=300)



class TaskHigherMathematics(models.Model):
 title = models.CharField(max_length=200)
 task = models.TextField
 result = models.CharField(max_length=300)

class TaskDiscretMath(models.Model):
 title = models.CharField(max_length=200)
 task = models.TextField
 result = models.CharField(max_length=300)

class TaskTheoryOfProbabilty(models.Model):
 title = models.CharField(max_length=200)
 task = models.TextField
 result = models.CharField(max_length=300)


