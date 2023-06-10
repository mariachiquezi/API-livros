import pyodbc


def conectar_banco():
    try:
        # para conectar con o banco de dados
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=;"
            "Database=PythonSQL;"

        )
        conexao = pyodbc.connect(dados_conexao)
        print("Conexão com o banco bem sucedida")
        cursor = conexao.cursor()
    except Exception as e:
        print("Erro ao conectar com banco de dados", e)
