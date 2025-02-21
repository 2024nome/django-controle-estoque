# PROJETO CONTROLE DE ESTOQUE

Descrição: processo para a criação de projeto

## PRE-REQUISITOS:
-VSCODE
-PYTHON 3.8 OU SUPERIOR
-DJANGO

### Steps para criação de um projeto
01. criação do repositorio(pasta) 
> mkdir nome_da_pasta
> ctrl+shift+n

02. Acessar o Repositorio
>cd nome_da_pasta

03. Criar o ambiente  virtual
>python -m venv nome_ambiente

04. acessar o ambiente virtual
- windows 
>.\nome_ambiente\Scripts\activate
- linux ou mac
>source nome_ambiente_virtual/bin/activate

05. instalar os pacotes (django...)
-Instalando um pacote especifico
> pip install django
- Instalando uma lista de pacote:
> pip install -r requeriments.txt

06. criação do projeto 
>django -admin startproject nome_projeto .

07. criação do app
> django-admin startapp nome_app

08. Criação do model.py [nome_app/models.py]  e configuração no arquivo 'setiings.py'


09. Realizar as migraçoes no banco de dados
-Faz as migrações dos models
> python manage.py makemigrations
- Aplica as migrações no banco de dados
> python manage.pt migrate

10.criar o Super Usuario
>python manage.py createsuperuser

11. criar as views e URLs
> Criar uma view no arquivo views.py do seu aplicativo
> Configurar as URLs no arquivo urls.py do seu aplicativo
> Adicionar as URLs do aplicativo no arquivo urls.py principal (do projeto)


12.  Continuar a Desenvolver
> Criar templates HTML para renderizar páginas dinâmicas.
> Configurar o banco de dados (por padrão, Django usa SQLite, mas você pode configurá-lo para usar outros como PostgreSQL ou MySQL).
> Adicionar formulários, autenticação de usuários, e muito mais.


13: startar o servidor de desevolvimento
> python manage.py runserver