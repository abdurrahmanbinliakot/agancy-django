from django.contrib import admin
from .models import Services, TeamMember, About, Clients, Portfolio
# Register your models here.
admin.site.register(Services)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(Clients)