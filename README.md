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

## Instalação 
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

Faça a migração do banco de dados:
~~~shell
python3 manage.py makemigrations
~~~

Em seguida:
~~~shell
python3 manage.py migrate
~~~

## Rodar o projeto

Digite o comando:
~~~shell
python3 manage.py runserver
~~~

<br />

Para acessar o website digite o seguinte link no navegador:
`127.0.0.1:8000`
