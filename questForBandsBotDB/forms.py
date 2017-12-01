from django import forms

from .models import *

class MemberForm(forms.ModelForm):

    class Meta:
        model = member
        fields = ('telegram_user_id', 'telegram_user_name', 'user_name')

class TeamForm(forms.ModelForm):

    class Meta:
        model = team
        fields = ('id_captain', 'name', 'descript')

class Team_memberForm(forms.ModelForm):

    class Meta:
        model = team_member
        fields = ('id_team', 'id_member')
