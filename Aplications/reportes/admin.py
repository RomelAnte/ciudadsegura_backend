from django.contrib import admin
from .models import Report, ReportType

# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'type', 'user', 'status', 'creation_date')
    readonly_fields = ('user', 'creation_date', 'update_date')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportType)