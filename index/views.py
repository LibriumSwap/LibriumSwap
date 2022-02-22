import requests
import json
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
		autor["imagem"] = '/static/images/autor_not_found.png'

	return render(request, "home/home.html", {
		"recentes": recentes,
		"autores_populares": autores_populares
		})

"""def get_wiki_main_image(title):
    url = 'https://en.wikipedia.org/w/api.php'
    data = {
        'action' :'query',
        'format' : 'json',
        'formatversion' : 2,
        'prop' : 'pageimages|pageterms',
        'piprop' : 'original',
        'titles' : title
    }
    response = requests.get(url, data)
    json_data = json.loads(response.text)
    
    if json_data['query']['pages'][0].get('original'):
    	return json_data['query']['pages'][0]['original']['source']
    else:
    	return "/static/images/autor_not_found.png"""