import pyautogui
import time

def clique_botao():

    botao_aceitar_localizacao = None #a variavel botão_aceitar_localização possui o valor "nenhum"

    print('Procurando o botão...')
    while botao_aceitar_localizacao is None: #enquanto o botão aindar estiver como none...
        botao_aceitar_localizacao = pyautogui.locateOnScreen('jogar.png', confidence=0.7) #procure na tela o botão e coloque na variavel botão_aceitar_localização
        time.sleep(1)

    print("Botão encontrado!") 
    botao_aceitar_centro = pyautogui.center(botao_aceitar_localizacao) #quando encontrar coloque na variavel botão_aceitar_centro o centro do botão_aceitar_localização
    pyautogui.click(botao_aceitar_centro) #clique no botão_aceitar_centro

    print("Partida aceita! Saindo...")
    time.sleep(5)
    exit()


clique_botao()