# Data Sources — Módulo 2: Bancos de Dados SQL

#MachineLearning #DataSources #SQL #Database

## O que é SQL?
- Linguagem para **consultar e manipular** bancos de dados relacionais
- Dados organizados em **tabelas** com linhas e colunas
- Essencial em ML para **buscar e preparar dados** antes de treinar modelos

## Princípio fundamental
> "Garbage in, garbage out" — a qualidade dos dados define a qualidade do modelo

## Ferramentas do mercado
- [[PostgreSQL]] → padrão em produção
- [[MySQL]] → comum em aplicações web
- [[SQLite]] → leve, sem servidor, ideal para aprender
- [[BigQuery]] → SQL em escala na nuvem (Google)

## Comandos essenciais

### Consulta básica
```sql
SELECT coluna1, coluna2 FROM tabela
WHERE condicao
ORDER BY coluna ASC/DESC;
```

### Agregação
```sql
SELECT coluna, COUNT(*) as total
FROM tabela
GROUP BY coluna;

SELECT coluna, AVG(coluna_numerica) as media
FROM tabela
GROUP BY coluna;
```

### JOIN — unir tabelas
```sql
SELECT a.col, b.col
FROM tabela_a as a
JOIN tabela_b as b ON a.id = b.fk_id;
```

## Integração com Python
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('banco.db')
df = pd.read_sql_query("SELECT * FROM tabela", conn)
```

## Fluxo no Pipeline de ML
SQL (buscar dados) → [[Pandas]] (processar) → Modelo ML

## Erros comuns
- Usar apelido sem definir com `as` no `FROM`
- Tentar ler tabela antes de criá-la
- Esquecer `GROUP BY` ao usar `COUNT` ou `AVG`

## Instalação
```bash
pip install pandas
# SQLite já vem com o Python
```