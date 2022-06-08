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
	if "subject" in request.GET or "teacher" in request.GET or "name" in request.GET:
		name_subject = request.GET.get("subject", "")
		name_teacher = request.GET.get("teacher", "")
		date_achievemebt = request.GET.get("name", "")
			#if name_subject == "" and name_teacher == "" and date_achievemebt == "":
			#	output = "{}".format(sort_data("all",[]))
		output =  "{0}, {1}, {2}".format(
									sort_data("subject", name_subject),
									sort_data("teacher", name_teacher),
									sort_data("name", date_achievemebt))
	else:
		output = "{}".format(sort_data_2())
	return HttpResponse(output, content_type="application/json")

def get_database(name_exel_base: str, name_base: str): # name_base - название базы которую хотим назвать
	"""Эта функция принимает название exel таблицы и название твое базы.
	И в результате создает файлы json и sql формата"""
	conn = sqlite3.connect("clubs.db") # создали файл пустой базы
	
	cursor = conn.cursor()
	cursor.execute("""SELECT * FROM mytable """)
	one_result = cursor.fetchall()

	subjects = dict()
	names = [description[0] for description in cursor.description]
	for i, value in enumerate(one_result):
		bas = dict()
		for j, item in enumerate(names):# создает словарь вида -> index: {id: x, some_name: name, ...}
			bas[item] = value[j]
		subjects[f"{i}"] = bas
	return subjects

	"""with open("clubs.json", "w") as write_file: # создаем файл json 
								json.dump(subjects, write_file)"""

def sort_data(title, objects: str):
	table = []
	b = ""
	objects_ = re.split(',', objects)
	for i in objects_:
		if title == "name":
			x = models.Mytable.objects.filter(name=i)
		if title == "teacher":
			x = models.Mytable.objects.filter(teacher=i)
		if title == "subject":
			if i == "science":
				b = "Научные"
			elif i == "sport":
				b = "Спортивные"
			elif i == "game":
				b = "Игровые"
			elif i == "info":
				b = "Программирование"
			x = models.Mytable.objects.filter(subject=b)
		if i == "":
			break
		else:
			for j in range(len(x)):
				table.append({x[j].id: [x[j].name, x[j].teacher, x[j].subject]})

	return json.dumps(table)

def sort_data_2():
	table = []
	x = models.Mytable.objects.all()
	for r in range(len(x)):
		table.append({x[r].id: [x[r].name, x[r].teacher, x[r].subject]})
	return table