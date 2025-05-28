# 🏎️ Projeto F1 - Dados da Fórmula 1 no PostgreSQL

Este projeto tem como objetivo **transformar arquivos CSV com dados históricos da Fórmula 1 em um banco de dados PostgreSQL**, facilitando a análise e visualização dos dados posteriormente no **Power BI**.

A ideia é centralizar os dados em um banco relacional, garantindo maior organização, integridade e flexibilidade para construir dashboards interativos com informações como:

* Corridas
* Pilotos
* Equipes
* Resultados
* Tempos de volta
* Paradas nos boxes
* Classificações e mais

Os dados são carregados a partir de arquivos `.csv` usando Python, `pandas` e `SQLAlchemy`.

---

## 🛠️ Instruções de Uso

### 1. Requisitos

* PostgreSQL instalado e rodando localmente
* Python 3.8 ou superior
* Instalar dependências:

```bash
pip install -r requirements.txt
```

---

### 2. Criar o banco de dados PostgreSQL

No seu PostgreSQL, crie um banco de dados com o nome `f1_db`:

```sql
CREATE DATABASE f1_db;
```

---

### 3. Estrutura esperada

Coloque todos os arquivos `.csv` na pasta `f1_data/` com os seguintes nomes:

```
circuits.csv
constructors.csv
constructor_results.csv
constructor_standings.csv
drivers.csv
driver_standings.csv
lap_times.csv
pit_stops.csv
qualifying.csv
races.csv
results.csv
seasons.csv
sprint_results.csv
status.csv
```

---

### 4. Executar o script de importação

Execute o arquivo Python para criar as tabelas e importar os dados:

```bash
python importador.py
```

---

### 🐳 Utilizando Docker para o PostgreSQL
Se você está usando Docker, o container do PostgreSQL pode ser iniciado com o seguinte comando:

```
docker run --name f1-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=f1_db -p 5432:5432 -d postgres
```
Isso cria um container com:

- Usuário: postgres

- Senha: postgres

- Banco de dados: f1_db

- Porta: 5432 exposta para conexão local

---


### 5. Conectar ao Power BI

No Power BI Desktop:

1. Clique em **Obter Dados** > **Banco de Dados PostgreSQL**.
2. Insira `localhost` como servidor e `f1_db` como nome do banco.
3. Conecte-se e selecione as tabelas desejadas para criar seus relatórios.

---

Se quiser, posso também gerar um script `.bat` ou `.sh` para automatizar esse processo. Deseja isso?
