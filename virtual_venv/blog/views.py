from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from . import models
import sqlite3
import json
import re

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})


words = {
	"physics": "физика",
	"info": "Информатика",
	"math": "Математика",
	"economycs": "Экономика",
	"bio": "Биология",
	"CTF": "CTF",
}
def getachievements(request):
	if "subject" in request.GET or "teacher" in request.GET or "event" in request.GET:
		name_subject = request.GET.get("subject", "")
		name_teacher = request.GET.get("teacher", "")
		event_achievemebt = request.GET.get("event", "")
		output =  "{}".format(
		sort_data_achievements("subject", name_subject),
		sort_data_achievements("teacher", name_teacher),
		sort_data_achievements("event", event_achievemebt))
	else:
		output = "{}".format(sort_data_all())
		
	return HttpResponse(output, content_type="application/json")

def get_database(title, objects: str): # name_base - название базы которую хотим назвать
	table = []
	b = ""
	objects_ = re.split(',', objects)
	for i in objects_:
		pass

def sort_data_achievements(title, objects: str):
	table = []
	objects_ = re.split(',', objects)
	for i in objects_:
		print(i)
		if title == "subject":
			values_lines = models.Olympiads.objects.filter(subject=words[i])
		elif title == "event":
			values_lines = models.Olympiads.objects.filter(event=words[i])
		elif title == "teacher":
			values_lines = models.Olympiads.objects.filter(subject=words[i])
		for r in range(len(values_lines)):
			x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].clas,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]
			table.append(x)
	return json.dumps(table)

def sort_data_all():
	table = []
	columns = [f.attname for f in models.Olympiads._meta.get_fields()]
	values_lines = models.Olympiads.objects.all()
	for r in range(len(values_lines)):
		x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].clas,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]
		table.append(x)
		
	return json.dumps(table)