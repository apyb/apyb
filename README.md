# APyB

[![Build Status](https://travis-ci.org/pythonbrasil/apyb.svg?branch=master)](https://travis-ci.org/pythonbrasil/apyb)
[![Coverage Status](https://coveralls.io/repos/github/pythonbrasil/apyb/badge.svg?branch=master)](https://coveralls.io/github/pythonbrasil/apyb?branch=master)

Novo site da Associação Python Brasil

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
-|-|-
ngapyb | nginx
psapyb | postgresql
dgapyb | gunicorn
