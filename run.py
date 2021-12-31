with open("autenticacao/models.py", "a") as f:
	f.write("\n\tfavoritos = models.ManyToManyField('livros.LivroAnuncio', blank=True)")