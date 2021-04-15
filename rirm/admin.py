from django.contrib import admin


from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'URL', 'phone_number')

admin.site.register(Register, RegisterAdmin)