from unittest import result
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

def gethobbies(request):
	if "subject" in request.GET:
		name_subject = request.GET.get("subject", "")
		output =  "{}".format(sort_data_hobbies("subject", name_subject),)
	elif "teacher" in request.GET :
		name_teacher = request.GET.get("teacher", "")
		output =  "{}".format(sort_data_hobbies("teacher", name_teacher))
	else:
		output = "{}".format(sort_data_all_hobbies())
		
	return HttpResponse(output, content_type="application/json")

def getachievements(request):
	if "subject" in request.GET:
		name_subject = request.GET.get("subject", "")
		output =  "{}".format(sort_data_achievements("subject", name_subject),)
	elif "teacher" in request.GET :
		name_teacher = request.GET.get("teacher", "")
		output =  "{}".format(sort_data_achievements("teacher", name_teacher))
	elif "level" in request.GET:
		level_achievement = request.GET.get("level", "")
		output =  "{}".format(sort_data_achievements("level", level_achievement))
	else:
		output = "{}".format(sort_data_all_achievements())
		
	return HttpResponse(output, content_type="application/json")

def filters_achievement(table):
	result_table = []
	columns = ['event', 'head_teacher', 'level', 'subject']
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
	columns = ['subject', 'teacher']
	columns_list = dict()
	del columns[0:2]
	values_lines = models.Mytable.objects.all()
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
			values_lines = models.Mytable.objects.filter(subject=i)
		elif title == "teacher":
			values_lines = models.Mytable.objects.filter(head_teacher=i)
		for r in range(len(values_lines)):
			x = [
			values_lines[r].name,
			values_lines[r].teacher,
			values_lines[r].subject,]
			table.append(x)
	result_table = filters_hobbies(table)
	return json.dumps(result_table)


def sort_data_achievements(title, objects: str):
	table = []
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "subject":
			values_lines = models.Olympiads.objects.filter(subject=i)
		elif title == "level":
			values_lines = models.Olympiads.objects.filter(level=i)
		elif title == "teacher":
			values_lines = models.Olympiads.objects.filter(head_teacher=i)
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
	result_table = filters_achievement(table)
	return json.dumps(result_table)

def sort_data_all_achievements():
	table = []
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
	result_table = filters_achievement(table)
	return json.dumps(result_table)

def sort_data_all_hobbies():
	table = []
	values_lines = models.Mytable.objects.all()
	for r in range(len(values_lines)):
		x = [
			values_lines[r].name,
			values_lines[r].teacher,
			values_lines[r].subject,]
		table.append(x)
	result_table = filters_hobbies(table)
	return json.dumps(result_table)