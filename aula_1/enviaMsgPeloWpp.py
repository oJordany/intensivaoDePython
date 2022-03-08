import pyautogui
import pyperclip
from time import sleep

pyautogui.PAUSE = 1

#Entrando no opera:
pyautogui.hotkey('alt', 'tab')
sleep(3)
pyautogui.click(x=12, y=254)
sleep(8)
for i in range(0, 3):
    pyautogui.press('tab')
pyperclip.copy('galeriba')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

texto = '''Se liga nessa mensagem que eu tô mandando pelo python! Depois vou te mandar um vídeo do pc mexendo sozinho pra te mandar a msg.'''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


#Comando para mapear a localização do mouse
#sleep(5)
#print(pyautogui.position())
