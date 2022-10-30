from django.contrib import admin
from .models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'date_of_birth', 'gender', 'address', 'city', 'state', 'pin', 'mobile', 'email', 'job_city', 'profile_img', 'resume', )
admin.site.register(Candidate, CandidateAdmin)