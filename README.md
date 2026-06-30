# Minha Solução — Sistema Bancário

---

## Tecnologias Utilizadas

### Backend
- Python 3.12
- FastAPI Standard v0.138.2
- Poetry

### Frontend
- React
- Vite
- NPM

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir instalado:

- Python 3.12+
- Poetry
- Node.js (versão LTS recomendada)
- NPM

---

# Executando o projeto

## 1. Backend (API)

Na pasta do backend, instale as dependências (caso ainda não tenha feito):

```bash
poetry install
```

Em seguida, inicie a aplicação:

```bash
poetry run fastapi dev
```

A documentação interativa da API ficará disponível em:

```
http://localhost:8000/docs
```

---

## 2. Frontend

Na pasta do frontend, instale as dependências:

```bash
npm install
```

Depois execute:

```bash
npm run dev
```

A aplicação estará disponível em:

```
http://localhost:5173
```

---

# 💡 Exemplo de utilização

## Criando uma conta

1. Informe o **nome do titular**.
2. Defina o **saldo inicial**.
3. Escolha o **tipo de conta**.
4. Clique em **Criar Conta**.

Após a criação, a conta será exibida na listagem.

Tipos de conta:

- **Checking** → Conta Corrente
- **Savings** → Conta Poupança

---

# Observações

O projeto cumpre seu objetivo funcional, porém ainda existem diversos pontos que podem ser aprimorados, como:

- Melhor organização dos Schemas da API;
- Validações mais robustas;
- Melhor modelagem das entidades;
- Tratamento de exceções mais completo;
- Testes automatizados;
- Maior separação de responsabilidades entre camadas da aplicação.

Uma arquitetura mais adequada para um ambiente de produção seria utilizar **Docker** para orquestrar toda a aplicação.

A estrutura poderia ser composta por:

- Um container para o Backend (FastAPI);
- Um container para o Frontend (React);
- Um container para o Banco de Dados;
- Um arquivo `docker-compose.yml` responsável por orquestrar todos os serviços.

Isso tornaria a configuração do ambiente muito mais simples, portátil e reproduzível.
