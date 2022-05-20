<div align="center">
   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" alt="Django" height="100" />
</div>

# Back-End Django
Esse projeto faz parte deste projeto: https://github.com/joaoygorr/E-Teacher

# Rodando o projeto
Crie um ambiente virtual para armazenar as dependências. Você pode criar usando esse comando: 
```
python -m venv env
```
Isso criará uma nova pasta `env` no seu diretório do seu projeto. Em seguida, ative-o com este comando no PowerShell ou CMD: 
```
.\env\scripts\activate.ps1 
```
```
.\env\scripts\activate.bat
```
Entre na pasta `server` e instale as dependências: 
```
pip install -r requirements.txt
```
Altere as configurações do banco de dados em `settings.py`.

Para rodar o projeto, execute: 
```
python manage.py runserver
```
