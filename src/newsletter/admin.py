from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    #code
    list_display = ["email", "full_name", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     #code
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)