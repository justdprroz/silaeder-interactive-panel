from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from . import models
import json
import re

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})

def getphoto(url):
	with open('static/media/clubs_photo/Го.jpg', "rb") as f:
		return HttpResponse(f.read(), content_type="image/jpeg")

def gethobbies(request):
	if request.GET.get("subject", "") != '':
		name_subject = request.GET.get("subject", "")
		output =  "{}".format(sort_data_hobbies("subject", name_subject),)
	else:
		output = "{}".format(sort_data_all_hobbies())
	return HttpResponse(output, content_type="application/json")

def getinternships():
	output = "{}".format(sort_data_all_internships())
		
	return HttpResponse(output, content_type="application/json")

def getachievements(request):
	if request.GET.get("subject", "") != '':
		name_subject = request.GET.get("subject", "")
		output = "{}".format(sort_data_achievements("subject", name_subject))
	elif request.GET.get("event", "") != '':
		event_achievement = request.GET.get("event", "")
		output = "{}".format(sort_data_achievements("event", event_achievement))
	elif request.GET.get("level", "") != '':
		level_achievement = request.GET.get("level", "")
		output = "{}".format(sort_data_achievements("level", level_achievement))
	else:
		output = "{}".format(sort_data_all_achievements())
		
	return HttpResponse(output, content_type="application/json")

def getconferences(request):
	if request.GET.get("subject", "") != '':
		name_subject = request.GET.get("subject", "")
		output = "{}".format(sort_data_conferences("subject", name_subject))
	elif request.GET.get("event", "") != '':
		event_achievement = request.GET.get("event", "")
		output = "{}".format(sort_data_conferences("event", event_achievement))
	elif request.GET.get("level", "") != '':
		level_achievement = request.GET.get("level", "")
		output = "{}".format(sort_data_conferences("level", level_achievement))
	else:
		output = "{}".format(sort_data_all_conferences())
		
	return HttpResponse(output, content_type="application/json")

def filters_achievement(table):
	result_table = []
	columns = ['event', 'level', 'subject']
	columns_list = dict()
	values_lines = models.Olympiads.objects.all()
	for j in range(len(columns)):
		a = []
		for g in range(len(values_lines)):
			a.append(values_lines.values_list(f"{columns[j]}", flat=True)[g])	
		columns_list[columns[j]] = list(set(a))
	result_table.append(table)
	result_table.append(columns_list)
	return result_table

def filters_hobbies(table):
	result_table = []
	columns = ['subject']
	columns_list = dict()
	values_lines = models.Hobbies.objects.all()
	for j in range(len(columns)):
		a = []
		for g in range(len(values_lines)):
			a.append(values_lines.values_list(f"{columns[j]}", flat=True)[g])	
		columns_list[columns[j]] = list(set(a))
	result_table.append(table)
	result_table.append(columns_list)
	return result_table

def filters_conferences(table):
	result_table = []
	columns = ['subject', 'level', 'event']
	columns_list = dict()
	values_lines = models.Conferences.objects.all()
	for j in range(len(columns)):
		a = []
		for g in range(len(values_lines)):
			a.append(values_lines.values_list(f"{columns[j]}", flat=True)[g])	
		columns_list[columns[j]] = list(set(a))
	result_table.append(table)
	result_table.append(columns_list)
	return result_table


def sort_data_hobbies(title, objects: str): # name_base - название базы которую хотим назвать
	table = []
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "subject":
			values_lines = models.Hobbies.objects.filter(subject=i)
		elif title == "teacher":
			values_lines = models.Hobbies.objects.filter(head_teacher=i)
		for r in range(len(values_lines)):
			url = f"<img src=virtual_venv\clubs_photo\{values_lines[r].name}.jpg"
			x = [
			values_lines[r].name,
			values_lines[r].teacher,
			values_lines[r].subject,]
			table.append(x)
	result_table = filters_hobbies(table)
	return json.dumps(result_table)

def sort_data_conferences(title, objects: str): # name_base - название базы которую хотим назвать
	table = []
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "subject":
			values_lines = models.Conferences.objects.filter(subject=i)
		elif title == "event":
			values_lines = models.Conferences.objects.filter(event=i)
		elif title == "level":
			values_lines = models.Conferences.objects.filter(level=i)
		for r in range(len(values_lines)):
			x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].class_field,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]
			table.append(x)
	result_table = filters_conferences(table)
	return json.dumps(result_table)


def sort_data_achievements(title, objects: str):
	table = []
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "subject":
			values_lines = models.Olympiads.objects.filter(subject=i)
		elif title == "level":
			values_lines = models.Olympiads.objects.filter(level=i)
		elif title == "event":
			values_lines = models.Olympiads.objects.filter(event=i)
		for r in range(len(values_lines)):
			x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].class_field,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]
			table.append(x)
	result_table = filters_achievement(table)
	return json.dumps(result_table)

def sort_data_all_achievements():
	table = []
	values_lines = models.Olympiads.objects.all()
	for r in range(len(values_lines)):
		x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].class_field,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]
		table.append(x)
	result_table = filters_achievement(table)
	return json.dumps(result_table)

def sort_data_all_hobbies():
	table = []
	values_lines = models.Hobbies.objects.all()
	for r in range(len(values_lines)):
		url = f"static/media/clubs_photo/{values_lines[r].name}.jpg"
		x = [
		values_lines[r].name,
		values_lines[r].teacher,
		values_lines[r].subject,]
		getphoto(url)
		table.append(x)		
	result_table = filters_hobbies(table)
	return json.dumps(result_table)

def sort_data_all_conferences():
	table = []
	values_lines = models.Conferences.objects.all()
	for r in range(len(values_lines)):
		x = [
			values_lines[r].date,
			values_lines[r].event,
			values_lines[r].class_field,
			values_lines[r].head_teacher,
			values_lines[r].level,
			values_lines[r].subject,
			values_lines[r].participants,
			values_lines[r].result,]	
		table.append(x)
	result_table = filters_conferences(table)
	return json.dumps(result_table)

def sort_data_all_internships():
	table = []
	result_table = []
	values_lines = models.Internships.objects.all()
	for r in range(len(values_lines)):
		x = [
			values_lines[r].date,
			values_lines[r].place,
			values_lines[r].feedback,
			values_lines[r].participant,]	
		table.append(x)
	result_table.append(table)
	result_table.append({})
	return json.dumps(result_table)