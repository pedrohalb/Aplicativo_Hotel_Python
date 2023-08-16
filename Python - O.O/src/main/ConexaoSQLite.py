import tkinter as tk
from tkinter import messagebox
import sqlite3

class ConexaoSQLite:
    def __init__(self):
        self.URL = "meu_banco_de_dados.db"
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = sqlite3.connect(self.URL)
            return self.conexao
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
            return None

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()

if __name__ == "__main__":
    conexao_sqlite = ConexaoSQLite()
    conexao = conexao_sqlite.conectar()

    if conexao:
        messagebox.showinfo("Sucesso", "Conexão com o banco de dados estabelecida.")
        # Aqui você pode realizar operações no banco de dados usando a conexão 'conexao'

        # Exemplo de criação de tabela
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")
        conexao.commit()

        # Exemplo de inserção de dados
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
        conexao.commit()

        # Exemplo de consulta de dados
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(resultado)

        # Fechar a conexão quando não precisar mais
        conexao_sqlite.fechar_conexao()
    else:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
