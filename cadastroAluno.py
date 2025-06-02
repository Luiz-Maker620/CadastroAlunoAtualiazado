#menu principal do sistema 

import sqlite3

#######################################
#   definicao de variaveis globais
#######################################



##############################################
### definicao de funcoes
##############################################
def main_menu():
    print("1, Cadastrar Aluno")
    print("2, Listar Alunos")
    print("3, Atualizar Aluno")
    print("4, Excluir Aluno")
    print("5, Sair")

    opcao = input("escolha uma opcao:")
    return opcao

##############################################
#   objetivo: conectar no namco de dados 
#   e criar as tabelas
##############################################
def create_Table(): 
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    idade INTEGER
                   )
        """) 
    conexao.commit()
    conexao.close()

def register(nome,email,idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
                       (nome,email,idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Email ja cadastrado")
    finally:
        conexao.close()


def display():
    conexao = sqlite3.connect("escola.db") #abri a conexao com o banco
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close() #feco a conexao com o banco

    print("lista de alunos cadastrados")
    
    for aluno in alunos:
        print(aluno)


def update(id,new_name,new_email,new_idade):
    
    conexao = sqlite3.connect("escola.db") #abrir a conexao com o banco  
    cursor = conexao.cursor() 

    cursor.execute("Update  aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                   (new_name,new_email,new_idade,id))
    
    conexao.commit() 
    conexao.close()
    print("Aluno atualizado com sucesso")

if __name__ == "__main__":
    create_Table()
    
    while True:
        opcao = main_menu()

        if opcao == "1":
            nome = input("Nome:")
            email = input("E-mail:")
            idade = int(input("Idade:"))
            register(nome,email,idade)
        elif opcao == "2":
            display()
        elif opcao == "3":
            id = int(input("Informe o ID do Aluno que vc quer atualizar:"))
            new_name = input("Novo Nome:")
            new_email = input("Novo E-mail:")
            new_idade = int(input("Nova Idade:"))
            update(id,new_name,new_email,new_idade)        
        elif opcao == "5":
            break
        else:
            print("Opcao Invalida")

