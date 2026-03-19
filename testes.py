import datetime

def testar_login(usuario, senha):
    usuario_correto = "admin"
    senha_correta = "1234"

    if usuario == usuario_correto and senha == senha_correta:
        return True
    return False

def executar_testes():
    testes = [
        ("admin", "1234"),
        ("admin", "errado"),
        ("user", "1234"),
        ("", ""),
    ]

    resultados = []

    for i, (user, senha) in enumerate(testes):
        resultado = testar_login(user, senha)
        status = "PASSOU" if resultado else "FALHOU"

        resultados.append({
            "teste": i+1,
            "usuario": user,
            "senha": senha,
            "resultado": status
        })

    return resultados

def gerar_relatorio(resultados):
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open("relatorio_testes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE TESTES AUTOMATIZADOS\n")
        arquivo.write(f"Data: {data}\n\n")

        for r in resultados:
            arquivo.write(
                f"Teste {r['teste']} | Usuário: {r['usuario']} | Resultado: {r['resultado']}\n"
            )

        total = len(resultados)
        sucessos = sum(1 for r in resultados if r["resultado"] == "PASSOU")

        arquivo.write("\nResumo:\n")
        arquivo.write(f"Total de testes: {total}\n")
        arquivo.write(f"Sucessos: {sucessos}\n")
        arquivo.write(f"Falhas: {total - sucessos}\n")

    print("Relatório gerado com sucesso!")

# Execução
resultados = executar_testes()

for r in resultados:
    print(r)

gerar_relatorio(resultados)