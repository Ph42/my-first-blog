from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *

def member_list(request):
	members = member.objects.order_by('registered_date')
	return render(request, 'questForBandsBotDB/member_list.html', {'members': members})

def team_list(request):
	teams = team.objects.order_by('created_date')
	return render(request, 'questForBandsBotDB/team_list.html', {'teams': teams})

def team_member_list(request):
	team_members = team_member.objects.order_by('id_team')
	return render(request, 'questForBandsBotDB/team_member_list.html', {'team_members': team_members})

def member_new(request):
	if request.method == "POST":
		form = MemberForm(request.POST)
		if form.is_valid():
			member = form.save(commit = True)
			return redirect('member_list')		
	else:
		form = MemberForm()
	return render(request, 'questForBandsBotDB/member_edit.html', {'form': form})

def team_new(request):
	if request.method == "POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			team = form.save(commit = True)
			return redirect('team_list')		
	else:
		form = TeamForm()
	return render(request, 'questForBandsBotDB/team_edit.html', {'form': form})

def team_member_new(request):
	if request.method == "POST":
		form = Team_memberForm(request.POST)
		if form.is_valid():
			team_member = form.save(commit = True)
			return redirect('team_member_list')		
	else:
		form = Team_memberForm()
	return render(request, 'questForBandsBotDB/team_member_edit.html', {'form': form})

def member_delete(request, pk):
	member = get_object_or_404(member, pk=pk)
	member.delete()
	members = member.objects.order_by('registered_date')
	return render(request, 'questForBandsBotDB/member_list.html', {'members': members})