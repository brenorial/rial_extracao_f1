# Usando Docker para rodar PostgreSQL

Você pode rodar o PostgreSQL facilmente com Docker.

## Comando para criar o container:

```
docker run --name f1-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=f1_db \
  -p 5432:5432 \
  -d postgres
```

Explicação

- POSTGRES_USER: usuário do banco (postgres)

- POSTGRES_PASSWORD: senha do usuário (postgres)

- POSTGRES_DB: banco criado automaticamente (f1_db)

- Porta 5432: exposta para conectar localmente

## Conectar no Python ou Power BI
Use o host localhost, porta 5432, usuário e senha postgres, banco f1_db.