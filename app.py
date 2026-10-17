from colorama import Fore, Style
niveis_agua = ["Muito Baixo (Critico)", "Baixo", "Medio", "Alto", "Muito Alto (Alerta)"]
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED 
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN 
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE   
for nivel in range(1, 6):
    mensagem = niveis_agua[nivel - 1]
    cor = definir_cor(nivel)
    print(f"{cor}{mensagem}{Style.RESET_ALL}")
    