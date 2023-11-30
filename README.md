# Tarefa4 - API Flask

Este repositório contém uma simples API Flask que realiza cálculos de fatorial e Fibonacci.

## Como Executar a Aplicação

### 1. Configuração do Ambiente Virtual

```bash
thiagoc@PhantomGray:~$ python3 -m venv NewWord
thiagoc@PhantomGray:~$ source NewWord/bin/activate
(NewWord) thiagoc@PhantomGray:~$ pip install Flask
(NewWord) thiagoc@PhantomGray:~$ cd /home/thiagoc/Documents/GitHub/tarefa4
(NewWord) thiagoc@PhantomGray:~/Documents/GitHub/tarefa4$ python app.py

```
A aplicação será iniciada e estará disponível em http://127.0.0.1:5000.

Em outra aba do terminal, você pode fazer solicitações usando curl. Por exemplo, para calcular o fatorial de 5:

```bash
thiagoc@PhantomGray:~/Documents/GitHub/tarefa4$ curl -i -X POST -H "Content-Type: application/json" -d '{"operacao": "fatorial", "numero": 5}' http://127.0.0.1:5000/calcular

```
