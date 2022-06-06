from django.shortcuts import render
from django.http import HttpResponse
from . import models

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})

class Achievements():
	def getachievements(request):
		name_subject = request.GET.get("subject", "")
		name_teacher = request.GET.get("teacher", "")
		date_achievemebt = request.GET.get("date", "")
		output =  "{0}, {1}, {2}".format(name_subject, name_teacher, date_achievemebt)
		return HttpResponse(output)
	
	def get_database(name_exel_base: str, name_base: str): # name_base - название базы которую хотим назвать
		"""Эта функция принимает название exel таблицы и название твое базы.
		И в результате создает файлы json и sql формата"""
		conn = sqlite3.connect(f"{name_base}.db") # создали файл пустой базы
		
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

		with open(f"{name_base}.json", "w") as write_file: # создаем файл json 
			json.dump(subjects, write_file)

	def sort_data(objects: str):
			con = sqlite3.connect(f"{name_base}.db")
			cur = con.cursor()
			objects_ = re.split(',', objects)
			x = dict()
			for i in range(1, len(objects_)):
					x[objects_[0]] = objects_[i]
			sort_list = []
			for i, value in enumerate(x):
				cursor.execute(f"""
						SELECT *
						FROM mytable
						WHERE ({value}='{x[value]}') """)
				pur = cursor.fetchall()
				sort_list.append(pur)
			return sort_list