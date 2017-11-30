from django.shortcuts import render
from django.utils import timezone
from .models import *

def member_list(request):
	members = member.objects.order_by('registered_date')
	return render(request, 'questForBandsBotDB/member_list.html', {'members': members})