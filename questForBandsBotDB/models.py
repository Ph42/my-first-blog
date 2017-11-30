from django.db import models
from django.utils import timezone


class state_of_team(models.Model):
	HAVE_ACTIVE_QUESTS = 'HAVE_ACTIVE_QUESTS'
	HAVE_NO_ACTIVE_QUESTS = 'HAVE_NO_ACTIVE_QUESTS'
	DELETED = 'DELETED'
	CHOICES = (
		(HAVE_ACTIVE_QUESTS, 'есть активные квесты'),
		(HAVE_NO_ACTIVE_QUESTS, 'нет активных квестов'),
		(DELETED, 'удалена'),		
		)
	descript = models.CharField(max_length = 50, choices = CHOICES, default = HAVE_NO_ACTIVE_QUESTS, unique = True)
	def publish(self):
		self.save()
	def __str__(self):
		return self.descript

class state_of_member(models.Model):
	ACTIVE = 'ACTIVE'
	DELETED = 'DELETED'
	CHOICES = (
		(ACTIVE, 'активен'),
		(DELETED, 'удалён'),			
		)
	descript = models.CharField(max_length = 50, choices = CHOICES, default = ACTIVE, unique = True)
	def publish(self):
		self.save()
	def __str__(self):
		return self.descript

class state_of_team_member(models.Model):
	ACTIVE = 'ACTIVE'
	DOES_NOT_RECIEVE_NOTES = 'DOES_NOT_RECIEVE_NOTES'
	DELETED_FROM_TEAM = 'DELETED_FROM_TEAM'
	TEAM_DELETED = 'TEAM_DELETED'
	CHOICES = (
		(ACTIVE, 'активен'),
		(DOES_NOT_RECIEVE_NOTES, 'не получает уведомления'),
		(DELETED_FROM_TEAM, 'удалён из команды'),	
		(TEAM_DELETED, 'команда удалена'),
		)
	descript = models.CharField(max_length = 50, choices = CHOICES, default = ACTIVE, unique = True)
	def publish(self):
		self.save()
	def __str__(self):
		return self.descript

class member(models.Model):
	id_state = models.ForeignKey('state_of_member', default = state_of_member.objects.get(descript = 'ACTIVE').id, on_delete = models.PROTECT)
	telegram_user_id = models.IntegerField(default = -1, unique = True)
	telegram_user_name = models.CharField(max_length = 50, unique = True)
	user_name = models.CharField(max_length = 50, blank = True)
	registered_date = models.DateTimeField(default = timezone.now)
	def publish(self):
		self.save()
	def __str__(self):
		return self.telegram_user_name

class team(models.Model):
	id_captain = models.ForeignKey('member')
	id_state = models.ForeignKey('state_of_team', default = state_of_team.objects.get(descript = 'HAVE_NO_ACTIVE_QUESTS').id, on_delete = models.PROTECT)
	name = models.CharField(max_length = 15, blank = True, unique = True)
	created_date = models.DateTimeField(default = timezone.now)
	descript = models.TextField(blank = True)
    
	def publish(self):
		self.save()
	def __str__(self):
		return self.name

class team_member(models.Model):	
	id_team = models.ForeignKey('team')
	id_member = models.ForeignKey('member')
	id_state = models.ForeignKey('state_of_team_member', default = state_of_team_member.objects.get(descript = 'ACTIVE').id, on_delete = models.PROTECT)
	def publish(self):
		self.save()
	def __str__(self):
		s = str(team.objects.get(pk = self.id_team.id).name) + '.' + str(member.objects.get(pk = self.id_member.id).telegram_user_name)
		return s