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
	description = models.CharField(max_length = 50, choices = CHOICES, default = HAVE_NO_ACTIVE_QUESTS)

class state_of_member(models.Model):
	ACTIVE = 'ACTIVE'
	DELETED = 'DELETED'
	CHOICES = (
		(ACTIVE, 'активен'),
		(DELETED, 'удалён'),			
		)
	description = models.CharField(max_length = 50, choices = CHOICES, default = ACTIVE)

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
	description = models.CharField(max_length = 50, choices = CHOICES, default = ACTIVE)

class member(models.Model):
	id_state = models.ForeignKey('state_of_member')

class team(models.Model):
    id_captain = models.ForeignKey('member')
    id_state = models.ForeignKey('state_of_team')
    '''
    text = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    '''
class team_member(models.Model):	
	id_team = models.ForeignKey('team')
	id_member = models.ForeignKey('member')
	id_state = models.ForeignKey('state_of_team_member')
