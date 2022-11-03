#A ideia do programa é simular um programa de arduino que seja capaz de obter dados de sensores diversos e ligar/ desligar equipamentos de uma estufa de cultivo de plantas. 
# Serão analisados temperatura do ar, umidade dos vasos e luminosidade do dia
# Ventiladores serão ligados ou desligados de acordo com a temperatura
# Luzes serão ligadas ou desligadas em dias nublados (abaixo da luminosidade ideal)
#Irrigação será ligada no nível mínimo, desligada no nível máximo, e ligada novamente apenas quando atingir o mínimo para evitar que as plantas fiquem submersas (não implementado ainda da forma correta)
# prints em caps lock são para indicar comandos ao hardware (liga, desliga) já que não é possível fazê-lo pelo python sem conectar a um hardware externo com um arduino por enquanto q
# leituras do sensor por enquanto colocadas no próprio script ou via comando sys para facilitar testes 
# 
# biblioteca para importar hora atual e adicioná-la ao registro

#void() # simulação da primeira parte do script do arduino
from datetime import datetime
now = datetime.now() #objeto para guardar data e hora atual para o log
date = now.strftime("%m/%d/%Y, %H:%M:%S") 

temp_max = 32 #max temp celsius aceitável
temp_min = 22 #min temp celsius de início dos fans

h2o_min = 45 # min teor água vaso aceitável (% Cap. Campo)
h2o_max = 90 #(capacidade de campo)

lux_min = 10000 # Luminosidade (em lux) mínima aceitável

log_dict = {} # dicionário para registro de eventos (luz baixa, temp alta e início das irrigações)
#variáveis obtidas pelo sensor 

temp = 33 #temp coletada pelo sensor
h2o = 30 # % h2o coletada pelo sensor
lux = 5000 #luminosidade coletada pelo sensor

#ou

#para checar mais rápido
# import sys
# print(sys.argv)
# temp = float(sys.argv[1])
# h2o = float(sys.argv[2])
# lux = float(sys.argv[3])


def loop(): #função que roda indefinidamente dentro do programa simulado de arduino
    def temperature(): 
        #função de ajuste da temperatura de acordo com leitura realizada
        # aciona 1o fan a partir de 22 graus
        #aciona 2o fan a partir de 28 graus
        # aciona 3o fan a partir de 32 graus, e adiciona ao registro log a data e a temperatura observada
        if temp >= temp_min:
            print("FAN 1 LIGADO")
            if temp >= 28:
                print("FAN 2 LIGADO")
                if temp >= temp_max:
                    print("FAN 3 LIGADO. \nObservação de Alta Temperatura Adicionada ao registro.")
                    log_dict["Data Temperatura Alta"] = date
        else:
            print("Temperatura ok")
            print("FANS DESLIGADOS")
    
    def lum(): #falta adicionar componente para evitar que a luz fique ligada por conta de ser noite 
        #garante suplementação luminosa em dias de baixa luminosidade
        #adiciona ao registro dia que ocorreu dia nublado
        if lux < lux_min:
            print("Luz muito baixa. Adicionando ao registro.\nSUPLEMENTAÇÂO LUMINOSA LIGADA")
            log_dict["Data dia Nublado"] = date
        else:
            print("Luminosidade ok")
            print("LUZES DESLIGADAS")

    
    def irriga(): 
        # a ideia é que o sistema irrigue quando chegue no nível mínimo, e continua irrigando até o nível máximo, então desliga até chegar no nível mínimo, e ligue apenas quando atingir o nível mínimo novamente, para que a planta não fique submersa o tempo inteiro. 
        #registra no log quando chegou no nível mínimo
        if h2o < h2o_min:
            print("Irrigação abaixo do mínimo. Ligando irrigação e Adicionando evento ao registro")
            print("IRRIGAÇÂO LIGADA")
            log_dict["Data Irrigação"] = date
        elif h2o >= h2o_min and h2o < h2o_max:
            print("Umidade ok")
        elif h2o >= h2o_max:
            print("Umidade na capacidade máxima")
            print("IRRIGAÇÂO DESLIGADA")

    # roda as funções definidas dentro do loop
    temperature()
    lum()
    irriga()
    print("Registro:", log_dict)

#roda o loop infinitamente 
loop()


    

