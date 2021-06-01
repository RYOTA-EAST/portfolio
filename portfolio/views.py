from django.shortcuts import render
from .models import Profile, Skill, Work
import datetime

def index(request):
  profile = Profile.objects.all().last()
  skills = Skill.objects.all().order_by('genre')
  works = Work.objects.all().order_by('-published')[:3]
  start_day = datetime.date(2020, 11, 21)
  days = (datetime.date.today() - start_day).days + 1

  context = {
    'profile': profile,
    'skills': skills,
    'works': works,
    'start_day': start_day,
    'days': days,
  }
  return render(request, 'index.html', context)

def works(request):
  works = Work.objects.all().order_by('-published')
  context = {
    'works':works,
  }
  return render(request, 'works.html', context)