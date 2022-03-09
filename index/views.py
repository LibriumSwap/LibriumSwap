import requests
import json
import wikipedia
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Count
from livros.models import LivroAnuncio


def index(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect("home")
	else:
		return render(request, "index/index.html")

def home(request):
	recentes = LivroAnuncio.objects.all().order_by('id')[:10]
	autores_populares = LivroAnuncio.objects.values("autor").order_by("autor").annotate(the_count=Count("autor"))
	autores_populares = autores_populares.order_by("-the_count")[:10]
	for autor in autores_populares:
		autor["imagem"] = "/static/images/autor_not_found.png"

	return render(request, "home/home.html", {
		"recentes": recentes,
		"autores_populares": autores_populares
		})


"""
WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='

def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results = 1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title = result[0])
        title = wkpage.title
        response  = requests.get(WIKI_REQUEST+title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']
        return img_link        
    except:
        return "/static/images/autor_not_found.png"
"""