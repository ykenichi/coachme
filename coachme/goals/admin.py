from django.contrib import admin
from goals.models import Goal, Step


class GoalAdmin(admin.ModelAdmin):
    pass


class StepAdmin(admin.ModelAdmin):
    pass


admin.site.register(Goal, GoalAdmin)
admin.site.register(Step, StepAdmin)
