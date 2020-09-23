# Teste Backend

## Apresentação

Documentação para utilização da Doc API - Desafio Backend.

## Autenticação

Para a utilização da API, é necessário criar um usuário no Django, via rota /admin/, e utilizar a rota de /login para ter acesso as demais rotas.

## Começando

Para acessar o sistema serão necessários os seguintes programas:

- [Python 3.7.5: necessário para a execução do sistema](https://www.python.org/downloads/)

Foi usado para teste de API o Postman, que pode ser baixado no link abaixo:
- [Postman, usado para teste da API](https://www.postman.com/downloads/)

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do Github em um diretório de sua preferência:

```commandline
cd "diretorio de sua preferencia"
git clone https://github.com/mcribeiro27/desafio-backend-1.git
```

## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto:

Para ambiente Unix

```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para ambiente Windows

```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

## Configuração

### Login

Está pasta realiza o login na Api – Desafio Backend.

### Login

```url
http://127.0.0.1:5000/login/
```

Para acesso é preciso passar os segintes dados:

### Body

```json

{
    "username": "nome_do_usuário",
    "password": "sua_senha"
}

```
irá criar um token, conforme mostrado abaixo.
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjAwODYzODE2LCJlbWFpbCI6Im1jcmliZWlybzI3QG91dGxvb2suY29tIn0.hh1ngFpjWLTX-JtOJEv94UD4Ti1Z9Fcdu2jUiy6WxOQ"
}
```
Para acesso as rotas é necessário copia-lo e colocálo no header com Authorization com a palavra JWT no inicio do token.
```
Autorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjAwODYzODE2LCJlbWFpbCI6Im1jcmliZWlybzI3QG91dGxvb2suY29tIn0.hh1ngFpjWLTX-JtOJEv94UD4Ti1Z9Fcdu2jUiy6WxOQ
```

### Classificação

Está pasta representa um objeto do tipo classificação na Doc Api – Desafio Backend.

### POST nova Classificação

```url
http://127.0.0.1:5000/classificacao/
```

Cadastra uma nova classificação no sistema

### Body

```json
{
    "classificacao":"trabalho"
}
```

### GET lista Classificação

```url
http://127.0.0.1:5000/classificacao/
```

Lista todas as classificacao no sistema

### Response

```json
[
    {
        "id": 1,
        "classificacao": "Trabalho"
    },
    {
        "id": 2,
        "classificacao": "Casa"
    }
]
```
### GET Busca classificação

```url
http://127.0.0.1:5000/classificacao/<int:id>/
```
Busca uma classificação no sistema

### Response

```json
{
    "id": 1,
    "classificacao": "Trabalho"
}
```
### PUT Atualiza Classificação

```url
http://127.0.0.1:5000/classificacao/<int:id>/
```
Modifica/atualiza uma classificação no sistema

### Body

```json
{
    "classificacao": "Caminho de casa"
}
```

### DELETE Apaga uma Classificação

```url
http://127.0.0.1:5000/classificacao/<int:id>/
```
Deleta uma classificação no sistema

### Viagem

Está pasta representa um objeto do tipo viagem na Doc Api – Desafio Backend.

### POST Nova Viagem

```url
http://127.0.0.1:5000/viagem/
```
Cadastra uma nova viagem no sistema

### Body

```json
{
    "dt_inicio": "20/03/2020",
    "dt_fim": "20/03/2020",
    "classificacao": 1,
    "nota": 5
}
```
### GET Lista Viagem

```url
http://127.0.0.1:5000/viagem/
```
Lista todas as viagens no sistema

### Response

```json
[ 
    {
        "id": 1,
        "dt_inicio": "20/03/2020",
        "dt_fim": "20/03/2020",
        "classificacao": 1,
        "nota": 5
    }
]
```
### GET Busca Viagem

```url
http://127.0.0.1:5000/viagem/<int:id>
```
Busca uma viagem no sistema

### Response

```json
{
    "id": 1,
    "dt_inicio": "20/03/2020",
    "dt_fim": "20/03/2020",
    "classificacao": 1,
    "nota": 5
}
```
### PUT Atualiza viagem

```url
http://127.0.0.1:5000/viagem/<int:id>
```
Modifica/atualiza uma viagem no sistema

### Body

```json
{
    "dt_inicio": "20/03/2021",
    "dt_fim": "20/03/2021",
    "classificacao": 2,
    "nota": 5
}
```
### DELETE Apaga viagem

```url
http://127.0.0.1:5000/viagem/<int:id>
```

Deleta uma viagem no sistema
