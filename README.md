
# LibriumSwap


## Sobre o projeto
Este foi um projeto para TCC do curso Desenvolvimento de Sistemas oferecido pela ETEC Uirapuru (Turma 2019-2021) <br/>
LibriumSwap é um website para venda e troca de livros físicos, visando em melhorar a circulação de livros pelo Brasil.

<br />

![Homepage LibriumSwap](https://raw.githubusercontent.com/LibriumSwap/LibriumSwap/main/presentation.jpg)


<br />

<br />

### Tecnologias

- **Python 3.8**
- Django
- SQLite
- HTML
- CSS
- ~~Docker~~

## Instalação em máquina local (TESTADO SOMENTE NO UBUNTU)
Siga os passos a seguir para instalar o projeto

<br />

Clone este repositório no seu dispositivo utilizando **git**:
~~~shell
git clone https://github.com/LibriumSwap/LibriumSwap
~~~

Após isso:
~~~shell
cd LibriumSwap
~~~
Para instalar todas as dependências necessárias para rodar o projeto:
~~~shell
pip3 install -r requirements.txt
~~~
Crie um arquivo **.env** dentro da pasta com as seguintes variáveis:

Para o **banco de dados** ([mais informações](https://docs.djangoproject.com/en/4.2/ref/databases/)):
~~~env
DB_ENGINE='[ENGINE DO SEU BANCO DE DADOS]'
DB_NAME='[NOME DO DB]'
DB_USER='[USUARIO]'
DB_PASSWORD='[SENHA]'
DB_HOST='[HOST]'
DB_PORT='[PORTA]'
~~~
Para o **envio de emails** ([mais informações](https://opensource.com/article/22/12/django-send-emails-smtp)):
~~~env
EMAIL_HOST_USER='[HOST]'
EMAIL_HOST_PASSWORD='[SENHA]'
~~~

**Token mercado pago**:
~~~env
MERCADO_PAGO_ACCESS_TOKEN='[SEU_TOKEN_MERCADO_PAGO]'
~~~

Faça a migração do banco de dados. :
~~~shell
python3 manage.py makemigrations autenticacao
~~~
Retire a comentação da linha 37 no arquivo livros.models, em seguida:
~~~shell
python3 manage.py makemigrations livros
~~~

Em seguida:
~~~shell
python3 manage.py migrate
~~~

## Rodar o projeto

Digite o comando:
~~~shell
gunicorn --bind 0.0.0.0:8000 LibriumSwap.asgi -w 4 -k uvicorn.workers.UvicornWorker
~~~

<br />

Para acessar o website digite o seguinte link no navegador:
`0.0.0.0:8000`
