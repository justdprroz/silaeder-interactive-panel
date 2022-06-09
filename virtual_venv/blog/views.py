from django.shortcuts import render
from django.http import HttpResponse
from . import models
import sqlite3
import json
import re

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})

#class Achievements():
def getachievements(request):
	if "subject" in request.GET or "teacher" in request.GET or "event" in request.GET:
		name_subject = request.GET.get("subject", "")
		name_teacher = request.GET.get("teacher", "")
		date_achievemebt = request.GET.get("event", "")
		output =  "{}".format(sort_data_achievements("subject", name_subject), sort_data_achievements("teacher", name_teacher))
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
	b = ""
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "event":
			x = models.Olympiads.objects.filter(event=i)
		if title == "teacher":
			x = models.Olympiads.objects.filter(head_teacher=i)
		if title == "subject":
			if i == "physics":
				b = "физика"
			elif i == "economy":
				b = "экономика"
			elif i == "math":
				b = "математика"
			elif i == "info":
				b = "Информатика"
			x = models.Olympiads.objects.filter(subject=b)
			b = []
			for i in x:
				b.append(i)
		if i == "":
			return {}
		else:
			for j in range(len(x)):
				table.append({title: [x[j].event, x[j].head_teacher, x[j].subject]})

	return json.dumps(table)

def sort_data_all():
	table = []
	columns = [f.attname for f in models.Olympiads._meta.get_fields()]
	for r in range(len(columns)):
		values_columns = list(models.Olympiads.objects.values_list(columns[r]))
		table.append({columns[r]: values_columns})
		
	return table