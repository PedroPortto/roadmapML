import sqlite3
import pandas as pd

# Cria o banco e as tabelas
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# Cria tabela de usuários
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    );

    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        genero TEXT,
        ano INTEGER
    );

    CREATE TABLE IF NOT EXISTS historico (
        usuario_id INTEGER,
        filme_id INTEGER,
        nota REAL
    );

    INSERT INTO usuarios VALUES (1, 'Ana', 28, 'São Paulo');
    INSERT INTO usuarios VALUES (2, 'Bruno', 17, 'Rio de Janeiro');
    INSERT INTO usuarios VALUES (3, 'Carla', 34, 'Curitiba');
    INSERT INTO usuarios VALUES (4, 'Diego', 22, 'São Paulo');

    INSERT INTO filmes VALUES (1, 'Inception', 'Ficção Científica', 2010);
    INSERT INTO filmes VALUES (2, 'Matrix', 'Ficção Científica', 1999);
    INSERT INTO filmes VALUES (3, 'O Poderoso Chefão', 'Drama', 1972);
    INSERT INTO filmes VALUES (4, 'Interestelar', 'Ficção Científica', 2014);
    INSERT INTO filmes VALUES (5, 'Coringa', 'Drama', 2019);

    INSERT INTO historico VALUES (1, 1, 9.5);
    INSERT INTO historico VALUES (1, 3, 8.0);
    INSERT INTO historico VALUES (2, 2, 7.5);
    INSERT INTO historico VALUES (3, 4, 9.0);
    INSERT INTO historico VALUES (3, 5, 6.5);
    INSERT INTO historico VALUES (4, 1, 8.5);
    INSERT INTO historico VALUES (4, 2, 9.0);
''')

conn.commit()
print("Banco criado com sucesso!")

##EXERCICIO 1
df = pd.read_sql_query('''
    SELECT nome, cidade
    FROM usuarios
    WHERE idade > 18
''',conn)
print(df)
print("---------------------------------------------------------------------------")

## EXERCICIO 2
df = pd.read_sql_query('''
    SELECT genero, COUNT(*) as total
    FROM filmes
    GROUP BY genero
''',conn)
print(df)
print("---------------------------------------------------------------------------")

#EXERCICIO 3
df = pd.read_sql_query('''
    SELECT u.nome, f.titulo, h.nota
    FROM historico as h
    JOIN filmes as f ON f.id = h.filme_id
    JOIN usuarios as u ON h.usuario_id = u.id
''',conn)
print(df)
print("---------------------------------------------------------------------------")

#EXERCICIO 4
df = pd.read_sql_query('''
    SELECT f.titulo, AVG(h.nota) as notaMedia
    FROM filmes as f
    JOIN historico as h ON h.filme_id = f.id
    GROUP BY f.titulo
    ORDER BY notaMedia ASC
''',conn)
print(df)
print("---------------------------------------------------------------------------")