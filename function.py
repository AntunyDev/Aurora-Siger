import data as d


def limpar_terminal():
    import subprocess
    import platform

    input("Pressione qualquer tecla para continuar...")

    sistema = platform.system()
    if sistema == "Windows":
        subprocess.run("cls", shell=True)  # Windows
    else:
        subprocess.run("clear", shell=True)  # Linux e Mac


def mostrar_hub_pre_decolagem():
    print("\n======== HUB - Pré-Decolagem ============\n")
    print("[1] Visualizar dados Telemetria")
    print("[2] Atualizar dados Telemetria manualmente")
    print("[3] Executar Análise energética")
    print("[4] Executar verificação de segurança")
    print("[5] Gerar relatório de pré-decolagem em csv")
    print("[6] Consultar análise por IA")
    print("[0] Sair")

    op = input("\nEscolha uma opção: ")
    return op


def visualizar_dados_telemetria(telemetria):
    print("\n======== DADOS DE TELEMETRIA ============\n")
    for chave, valor in telemetria.items():
        print(f"{chave.replace('_', ' ').title()}: {valor}")
    print("\n----------------------------\n")


def atualizar_dados_telemetria_manual(telemetria):
    print("\n======== ATUALIZAR DADOS DE TELEMETRIA MANUALMENTE ============\n")
    print("[1] - Temperatura Interna")
    print("[2] - Temperatura Externa")
    print("[3] - Integridade Estrutural")
    print("[4] - Nível de Energia")
    print("[5] - Pressão dos Tanques")
    print("[6] - Status dos Módulos Críticos")
    print("[7] - Atualizar todos os dados")
    print("[0] - Voltar")

    op = input("\nEscolha o dado que deseja atualizar: ")

    if op == "1":
        novo_valor = input("Digite a nova temperatura interna (°C): ")
        telemetria["temperatura_interna"] = float(novo_valor)
    elif op == "2":
        novo_valor = input("Digite a nova temperatura externa (°C): ")
        telemetria["temperatura_externa"] = float(novo_valor)
    elif op == "3":
        novo_valor = input("Digite a nova integridade estrutural (0-100): ")
        telemetria["integridade_estrutural"] = float(novo_valor)
    elif op == "4":
        novo_valor = input("Digite o novo nível de energia (0-100): ")
        telemetria["nivel_energia"] = float(novo_valor)
    elif op == "5":
        novo_valor = input("Digite a nova pressão dos tanques (psi): ")
        telemetria["pressao_tanques"] = float(novo_valor)
    elif op == "6":
        novo_valor = input("Digite o novo status dos módulos críticos (0-100): ")
        telemetria["status_modulos_criticos"] = float(novo_valor)
    elif op == "7":
        novo_valor = input("Digite a nova temperatura interna (°C): ")
        telemetria["temperatura_interna"] = float(novo_valor)
        novo_valor = input("Digite a nova temperatura externa (°C): ")
        telemetria["temperatura_externa"] = float(novo_valor)
        novo_valor = input("Digite a nova integridade estrutural (0-100): ")
        telemetria["integridade_estrutural"] = float(novo_valor)
        novo_valor = input("Digite o novo nível de energia (0-100): ")
        telemetria["nivel_energia"] = float(novo_valor)
        novo_valor = input("Digite a nova pressão dos tanques (psi): ")
        telemetria["pressao_tanques"] = float(novo_valor)
        novo_valor = input("Digite o novo status dos módulos críticos (0-100): ")
        telemetria["status_modulos_criticos"] = float(novo_valor)
    elif op == "0":
        return
    else:
        print("Opção inválida.")
