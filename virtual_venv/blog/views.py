from django.shortcuts import render

def main(request):
    return render(request, 'blog/post_kist.html', {})

def achievements(request):
	return render(request, 'blog/achievements.html', {})