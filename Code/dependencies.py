'''
Esse código tem como função manipular o tempo de envio de dados do modbus slave simulator.
Author: Gabriela Dellamora Paim
Version: 03.08.23
E-mail: gabrieladellamora@gmail.com 
Github: https://github.com/MarnieGrenat
'''
import pyautogui as pag
import pydirectinput as pdi
from time import sleep


def configuration(limit_burst, limit_periodo, tempo_burst, tempo_periodo, ciclos_burst, ciclos_periodo) -> list:
    config = input('Gostaria de configurar os valores? (s/n): ')
    
    if config in ['s', 'S', 'sim', 'Sim', 'SIM', 'y', 'Y', 'yes', 'Yes', 'YES', 1]:  
        print('Iniciando configuração de valores')
        sleep(1)
    
        print('Agora vamos configurar o limite. É quantas vezes o ciclo vai se repetir. Exemplo: 10 ciclos de 10 segundos = 100 segundos')  
        limit_burst = input('\nDigite o limite de ciclos Burst desejado e aperte "enter": ')
        limit_periodo = input('Digite o limite de ciclos Periódicos desejado e aperte "enter": ')
        sleep(1)
        print('\nValores de limite configurados:')
        print('Valor de limite do limite de Burst: ', limit_burst)
        print('Valor de limite do limite de Periódicos: ', limit_periodo)
        sleep(1)
        
        print('\nAgora vamos configurar o tempo. É o tempo de espera entre cada ciclo.')
        tempo_burst = input('\nDigite o tempo de espera entre cada ciclo de Burst e aperte "enter": ')
        tempo_periodo = input('Digite o tempo de espera entre cada ciclo de Periódicos e aperte "enter": ')
        sleep(1)
        print('\nValores de tempo configurados:')
        print('Valor de tempo do ciclo Burst: ', tempo_burst)
        print('Valor de tempo do ciclo Periódicos: ', tempo_periodo)
        sleep(1)
        
        print('\nAgora vamos configurar o número de ciclos. É quantas vezes os números serão modificados dentro do ciclo de modificação.')
        ciclos_burst = input('\nDigite o número de ciclos Burst e aperte "enter": ')
        ciclos_periodo = input('Digite o número de ciclos Periódicos e aperte "enter": ')
        sleep(1)
        print('\nValores de ciclos configurados:')
        print('Valor de ciclos do ciclo Burst: ', ciclos_burst)
        print('Valor de ciclos do ciclo Periódicos: ', ciclos_periodo)
        
        print('Valores configurados com sucesso!')
        sleep(2)
        
    if config in ['n', 'N', 'nao', 'Não', 'NÃO', 'Não', 'NAO', 'no', 'No', 'NO', 0]:
        print('Valores padrão selecionados')
        
        print('\nValor de limite do ciclo Burst: ', limit_burst)
        print('Valor de limite do ciclo Periódicos: ', limit_periodo)
        
        print('\nValor de tempo do ciclo Burst: ', tempo_burst)
        print('Valor de tempo do ciclo Periódicos: ', tempo_periodo)
        
        print('\nValor de ciclos do ciclo Burst: ', ciclos_burst)
        print('Valor de ciclos do ciclo Periódicos: ', ciclos_periodo)
    
    else:
        print('Opção inválida. Valores padrão selecionados')
    
        print('\nValor de limite do ciclo Burst: ', limit_burst)
        print('Valor de limite do ciclo Periódicos: ', limit_periodo)
        
        print('\nValor de tempo do ciclo Burst: ', tempo_burst)
        print('Valor de tempo do ciclo Periódicos: ', tempo_periodo)
        
        print('\nValor de ciclos do ciclo Burst: ', ciclos_burst)
        print('Valor de ciclos do ciclo Periódicos: ', ciclos_periodo)
    print('\n\n\n\n\n\n')
    print('Iniciando script em 5 segundos. Posicione o mouse no campo de entrada de dados do Modbus Slave Simulator. ou aperte "ctrl + c" para cancelar.')
    sleep(1)
    return [limit_burst, limit_periodo, tempo_burst, tempo_periodo, ciclos_burst, ciclos_periodo]

def main(limit_b=51, limit_p=360, tempo_b=1, tempo_p=5, ciclo_b=10, ciclo_p=5):
    log = ''
    # Starting script in 5 seconds
    for i in range(5,0,-1):
        print(f'Starting in {i} seconds...')
        sleep(1)
    print('Start!')
    sleep(1)


    # Burst Test
    print('Teste Burst iniciado')
    log+='Teste Burst iniciado\n'
    for ciclo in range(limit_b):
        for i in range(1, (ciclo_b+1)):
            pag.write(f'{i}', interval=0.15)
            pdi.press('enter')
            sleep(tempo_b)
            
        ciclo+=1
        print(f'ongoing ciclo Burst: {ciclo}')
        log += f'ongoing ciclo Burst: {ciclo}\n'
        sleep(60)


    # Wait for 5 minutes 
    log+=('Iniciando espera de 5 minutos. Valor do gráfico = -1')
    print(' Iniciando espera de 5 minutos. Valor do gráfico = -1')

    pag.write(f'{-1}', interval=0.15)
    #write -1 para facilitar a diferenciação no gráfico

    pdi.press('enter')
    #Dar um tempo (5 minutos) para facilitar a diferenciação no gráfico
    sleep (300)

    log+=('Iniciando espera de 5 minutos. Valor do gráfico = -1')
    print(' Iniciando espera de 5 minutos. Valor do gráfico = -1')

    # Ciclo periódico de 10s
    print('Teste Periódico iniciado')
    log+='Teste Periódico iniciado\n'
    for ciclo in range(limit_p):
        for i in range(1, (ciclo_p+1)):
            pag.write(f'{i}', interval=0.15)
            pdi.press('enter')
            sleep(tempo_p)
            
        print(f'ongoing ciclo {tempo_p}s: {ciclo}')
        log += f'ongoing ciclo {tempo_p}s: {ciclo}\n'
        
    print(50*'-')
    print('Ciclo Burst: ', limit_b)
    print(f'Ciclo {tempo_p}s: ', limit_p)

    log += (50*'-')
    log += f'Ciclo Burst: {limit_b}\n'
    log += f'Ciclo {tempo_p}s: {limit_p}\n'

    with open(r'.\log_onchange_script.txt', 'w') as f:
        f.write(log)
        f.close()
    print('End!')