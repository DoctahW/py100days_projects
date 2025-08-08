import random

def card_sel():
    """Seleciona e retorna uma carta aleatória do baralho."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 é o Ás
    return random.choice(cards)

def calcular_soma(cartas):
    """
    Calcula a soma das cartas. Se a soma passar de 21 e houver um Ás (11)
    """
    if sum(cartas) > 21 and 11 in cartas:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def comparar_resultados(soma_player, soma_computer):
    """
    Compara a pontuação final do jogador e do computador e retorna a mensagem de resultado.
    """
    if soma_player > 21:
        return "Você Perdeu! Passou de 21."
    if soma_computer > 21:
        return "Você ganhou! O computador passou de 21."
    if soma_player == soma_computer:
        return "Empate!"
    elif soma_player == 21:
        return "Você ganhou! Você tirou 21 (Blackjack)."
    elif soma_computer == 21:
        return "Você perdeu! O computador tirou 21 (Blackjack)."
    elif soma_player > soma_computer:
        return "Você ganhou! Sua pontuação é maior."
    else:
        return "Você perdeu! A pontuação do computador é maior."
def play_game():
    player = []
    computer = []
    game_over = False

    sel = input("Você quer jogar um jogo de '21'? Digite 'S' ou 'N':\n").upper()

    if sel == 'S':
        for _ in range(2):
            player.append(card_sel())
            computer.append(card_sel())
            
        while not game_over:
            soma_player = calcular_soma(player)
            soma_computer = calcular_soma(computer)
            
            print(f"\nSuas cartas: {player}. Total: {soma_player}")
            print(f"Carta da Máquina: [{computer[0]}, ?]")

            if soma_player == 21 or soma_player > 21:
                game_over = True
            else:
                retry = input("Você quer outra carta? 'S' ou 'N'? \n").upper()
                if retry == 'S':
                    player.append(card_sel())
                else:
                    game_over = True
        
        soma_computer = calcular_soma(computer)
        while soma_computer < 17 and soma_computer != 0:
            computer.append(card_sel())
            soma_computer = calcular_soma(computer)

        print("-" * 30)
        final_player = calcular_soma(player)
        final_computer = calcular_soma(computer)
        
        print(f"Suas cartas finais: {player}. Total: {final_player}.")
        print(f"Cartas da máquina: {computer}. Total: {final_computer}.")
        
        resultado = comparar_resultados(final_player, final_computer)
        print(f"\n>> {resultado} <<")

        retry_game = input("Você quer jogar novamente? 'S' ou 'N'? \n").upper()
        if retry_game == 'S':
            play_game()
        else:
            print("Ok, até a próxima!")
    else:
        print("Ok, até a próxima!")
play_game()