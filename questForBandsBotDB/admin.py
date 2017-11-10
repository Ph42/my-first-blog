from django.contrib import admin
from .models import *

admin.site.register(state_of_team)
admin.site.register(state_of_member)
admin.site.register(state_of_team_member)
admin.site.register(member)
admin.site.register(team)
admin.site.register(team_member)

# Register your models here.
