import function as fcs
import data as d

op = fcs.mostrar_hub_pre_decolagem()

while True:
    if op == "1":
        fcs.visualizar_dados_telemetria(d.telemetria)
    elif op == "2":
        print("\nOpção de atualização manual ainda não implementada.")
    elif op == "3":
        print("\nOpção de análise energética ainda não implementada.")
    elif op == "4":
        print("\nOpção de verificação de segurança ainda não implementada.")
    elif op == "5":
        print("\nOpção de geração de relatório em csv ainda não implementada.")
    elif op == "6":
        print("\nOpção de consulta por IA ainda não implementada.")
    elif op == "0":
        print("\nSaindo do HUB de pré-decolagem. Até a próxima!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
