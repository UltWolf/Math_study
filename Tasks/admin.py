from django.contrib import admin
from Tasks.models import TaskDiscretMath,TaskHigherMathematics,TaskTheoryOfProbabilty,MathTask
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register( TaskDiscretMath)
admin.site.register(TaskHigherMathematics)
admin.site.register(TaskTheoryOfProbabilty)
admin.site.register(MathTask)