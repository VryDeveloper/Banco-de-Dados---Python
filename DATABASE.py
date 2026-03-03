import sqlite3

banco = sqlite3.connect('Valorant.db')
cursor = banco.cursor()

op = 0  

while op != 4:
    print("Banco de Dados #1 - Armas do Valorant")
    print("1. Ver Armas")
    print("2. Adicionar Arma")
    print("3. Excluir Arma")
    print("4. Sair")
    
    op = int(input("Selecione: "))
    
    if op == 1:
        cursor.execute("SELECT * FROM VALORANT_GUNS")
        print(cursor.fetchall())
        
    elif op == 2:
        inserir_arma_nome = input("Digite o Nome: ")
        inserir_tipo_arma = input("Digite o Tipo da arma: ")


        cursor.execute("""
            INSERT INTO VALORANT_GUNS (Nome_Arma, Tipo_De_Arma) 
            SELECT ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM VALORANT_GUNS WHERE Nome_Arma = ?)""",
            (inserir_arma_nome, inserir_tipo_arma, inserir_arma_nome))
        banco.commit()
        print("Arma adicionada com sucesso!")
        
    elif op == 3:
        arma_deletada = input("Digite o nome da arma a deletar: ")
        cursor.execute("DELETE FROM VALORANT_GUNS WHERE Nome_Arma = ?", (arma_deletada,))
        banco.commit()
        print(f"A arma {arma_deletada} foi deletada com sucesso!")
        
    elif op == 4:
        print("Saindo...")
        
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

banco.close()
