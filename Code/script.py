from dependencies import *
'''
Esse código tem como função manipular o tempo de envio de dados do modbus slave simulator.
Author: Gabriela Dellamora Paim
E-mail: gabrieladellamora@gmail.com
Github: https://github.com/MarnieGrenat
Version: 03.08.23
'''

# É possível configurar por dentro do script. Evite mexer no código fonte do script.py ou dependencies.py.

#limit_burst = 51 # Mais ou menos 1 hora de 70 em 70 segundos
#limit_periodo = 360 # Mais ou menos 1 hora de 10 em 10 segundos

#tempo_burst = 1 #segundos de espera burst
#tempo_periodo = 5 #segundos de espera período

#ciclos_burst = 10# Quantos números serão modificados dentro do ciclo de modificação rajada
#ciclos_periodo = 5# Quantos números serão modificados dentro do ciclo de modificação periódica

if __name__ == "__main__":
    param = list(configuration(51, 360, 1, 5, 10, 5))
    main(param[0], param[1], param[2], param[3], param[4], param[5])
