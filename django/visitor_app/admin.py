from django.contrib import admin
from visitor_app.models import VisitFor,Department,Visitor,Visit

class VisitAdmin(admin.ModelAdmin):
	pass

class VisitForAdmin(admin.ModelAdmin):
	pass

class DepartmentAdmin(admin.ModelAdmin):
	pass

class VisitorAdmin(admin.ModelAdmin):
	pass


admin.site.register(Visit,VisitAdmin)
admin.site.register(VisitFor,VisitForAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Visitor,VisitorAdmin)

