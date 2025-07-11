import pyodbc

def get_connection():
    connection = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=192.168.9.200,1433;"  # Atualize para o seu servidor
        "Database=DB_VIEWS;"       # Atualize para o seu banco de dados
        "UID=Logistica_OPCD;"
        "PWD=Log1_Op@CD123;"
        "LoginTimeout=60;" # Adicione esta linha"
    )
    return connection
# Bloco para testar a conexão

if __name__ == "__main__":
    try:
        connection = get_connection()
        print("Conexão estabelecida com sucesso!")
        connection.close()
    except Exception as e:
        print(f"Erro ao conectar: {e}")


