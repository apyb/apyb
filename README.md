# APyB

[![Build Status](https://travis-ci.org/pythonbrasil/apyb.svg?branch=master)](https://travis-ci.org/pythonbrasil/apyb)
[![Coverage Status](https://coveralls.io/repos/github/pythonbrasil/apyb/badge.svg?branch=master)](https://coveralls.io/github/pythonbrasil/apyb?branch=master)

Novo site da Associação Python Brasil

## Ambiente de desenvolvimento

Durante o desenvolvimento, você pode utilizar
[`pip`](https://pip.pypa.io/en/stable/installing/) ou
[`pipenv`](https://pipenv.readthedocs.io/en/latest/) ou mesmo
[`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

1. Crie o virtualenv com sua ferramenta favorita.
2. Instale as dependências de desenvolvimento com
   `pip install -r requirements-dev.txt` ou, se estiver
   usando `pipenv`, utilize
   `pipenv install -r requirements-dev.txt`.
3. Com o ambiente criado, você precisa definir a variável de ambiente que
   indica qual configuração será usada. Para desenvolvimento, utilize
   `export DJANGO_SETTINGS_MODULES=apyb.settings.dev`.
4. Para iniciar o servidor, utilize `python manage.py runserver`; `manage.py`
   se encontra dentro do diretório `apyb`.

Este projeto utiliza [EditorConfig](https://editorconfig.org/) para manter o
padrão dos editores. Verifique se o seu tem suporte embutido ou se você precisa
instalar algum plugin.

## Instalação

### Requisitos

#### Local

Python >=3.7
PostgreSQL >=10.5

#### Docker

docker-ce >=18

##### Gerando as imagens locais necessárias

```sh
docker-compose build
```

##### Executando dentro do container em primeiro plano

```sh
docker-compose up
```

##### Executando em segundo plano

```sh
docker-compose up -d
```

###### Estrutura do docker

container | serviço
-|-
ngapyb | nginx
psapyb | postgresql
dgapyb | gunicorn
