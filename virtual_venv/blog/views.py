from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})

def getachievements(request):
	name_subject = request.GET.get("subject", "")
	name_teacher = request.GET.get("teacher", "")
	date_achievemebt = request.GET.get("date", "")
	output = "<h2> Category: {0}, {1}, {2} </h2>".format(name_subject, name_teacher, date_achievemebt)
	return HttpResponse(output)