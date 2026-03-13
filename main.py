import function as fcs
import data as d
import csv

while True:
    fcs.limpar_terminal()
    op = fcs.mostrar_hub_pre_decolagem()

    if op == "1":
        fcs.visualizar_dados_telemetria(d.telemetria)
        fcs.limpar_terminal()
    elif op == "2":
        fcs.atualizar_dados_telemetria_manual(d.telemetria)
        fcs.limpar_terminal()
    elif op == "3":
        fcs.executar_analise_energetica(d.telemetria)
        fcs.limpar_terminal()
    elif op == "4":
        fcs.executar_verificacao_seguranca(d.telemetria)
        fcs.limpar_terminal()
    elif op == "5":
        fcs.gerar_relatorio_csv(d.telemetria)
        fcs.limpar_terminal()
    elif op == "6":
        fcs.consultar_analise_ia(d.telemetria)
        fcs.limpar_terminal()
    elif op == "0":
        print("\nSaindo do HUB de pré-decolagem. Até a próxima!")
        fcs.limpar_terminal()
        break
    elif op == "7":
        fcs.analise_assistida_ia_simulada(d.telemetria)
        fcs.limpar_terminal()
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
        fcs.limpar_terminal()
