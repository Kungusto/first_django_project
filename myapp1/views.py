from django.shortcuts import render

def index_page (request) : # HTTP-запрос
    return render(request, 'index.html', context={'data':5}) # HTTP-ответ. выдает нам страничку index_html

