'''
Esse código tem como função manipular o tempo de envio de dados do modbus slave simulator.
Author: Gabriela Dellamora Paim
Version: 14.07.23
Github: https://github.com/MarnieGrenat
'''
import pyautogui as pag
import pydirectinput as pdi
from time import sleep

# Quantas vezes o ciclo será executado
limit1 = 51 # Mais ou menos 1 hora de 70 em 70 segundos
limit2 = 360 # Mais ou menos 1 hora de 10 em 10 segundos

CICLO_BURST = 0
CICLO_DEFAULT = 0
log = ''

for i in range(5,0,-1):
    print(f'Starting in {i} seconds...')
    sleep(1)
print('Start!')

while True:
    if CICLO_BURST == limit1:
        break
    for i in range(1, 11):
        pag.write(f'{i}', interval=0.15)
        pdi.press('enter')
        sleep(1)
        
    CICLO_BURST+=1
    print(f'ongoing ciclo Burst: {CICLO_BURST}')
    log += f'ongoing ciclo Burst: {CICLO_BURST}\n'
    sleep(60)


#write -1 para facilitar a diferenciação no gráfico
pag.write(f'{-1}', interval=0.15)
pdi.press('enter')
#Dar um tempo (5 minutos) para facilitar a diferenciação no gráfico
sleep (300)


# Ciclo periódico de 10s
while True:
    if CICLO_DEFAULT == limit2:
        break
    for i in range(1, 6):
        pag.write(f'{i}', interval=0.15)
        pdi.press('enter')
        sleep(5)
        
    CICLO_DEFAULT+=1
    print(f'ongoing ciclo 10s: {CICLO_DEFAULT}')
    log += f'ongoing ciclo 10s: {CICLO_DEFAULT}\n'
    
print(50*'-')
print('Ciclo Burst: ', CICLO_BURST)
print('Ciclo 10s: ', CICLO_DEFAULT)

log += (50*'-')
log += f'Ciclo Burst: {CICLO_BURST}\n'
log += f'Ciclo 10s: {CICLO_DEFAULT}\n'

with open(r'.\log_onchange_script.txt', 'w') as f:
    f.write(log)
    f.close()
print('End!')
