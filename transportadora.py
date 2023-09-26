#------------------------- função para verificar a dimensão do objeto, com input e utilizando os if e elif para a validação confome as exigencias da atividade
def dimObj(): 
    while True:
        try:       
            comp = float(input("Digite o comprimento do objeto (em cm): "))
            print("=" * 45)   
            lar = float(input("Digite a largura do objeto (em cm): ")) 
            print("=" * 45)
            alt = float(input("Digite o comprimento do objeto (em cm): ")) 
            print("=" * 45)
            volume = alt*lar*comp     
            print(f"O volume do objeto em cm é: {volume:.2f}") 
            print("=" * 45)
            if volume < 1000:
                return 10.00   
            elif 1000 <= volume < 10000:
                return 20.00
            elif 10000 <= volume < 30000:
                return 30.00
            elif 30000 <= volume < 100000:
                return 50.00
            elif volume >= 100000:   
                print(" a dimensão dada ultrapassa o limite permitido.")
                continue
        except:  
            print("Você digitou a dimensão do objeto com um valor não numérico.")
            continue
#---------------------------------------------------------------------------------------------
#                                                       função para receber o peso dos objetos e fazer a validação para que se ultrapasse de 30, dê erro, ultilizando o return também 
#                                                       para retornar o valor para fora da função

def pesoObj():  
  while True:
      try: 
            peso = float(input("Entre com o peso do Objeto (em kg): "))  
            if peso < 0.1:
                return 1.0     
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2.0
            elif 10 <= peso < 30:
                return 3.0
            elif peso > 30: 
                print("o peso ultrapassou o limite permitido.")
            continue

      except:  
            print("Você digitou o peso do objeto com valor não numérico.")
            continue
#---------------------------------------------------------------------------------------------
#---------------------------------------------------- função para receber a rota desejada, retornando o respectivo valor da escolha do usuario
#                                                     apresentando uma mensagem de erro, para caso a sigla da rota seja digitado
def rotaObj():  
    while True:
        print("=" * 45)
        print("Escolha a rota desejada:  ") 
        print(" BR - De Brasilia para o Rio de Janeiro")
        print(" BS - De Brasilia para São Paulo")
        print(" RB - Do Rio de Janeiro para Brasilia")
        print(" SR - De São Paulo para Rio de Janeiro")
        print(" RS - Do Rio de janeiro para São Paulo")
        print(" SB - De São paulo para brasilia")
        print("=" * 45)
        rotaObjto = input("Você escolheu a rota: ")
        print("=" * 45)
        if rotaObjto == "BR":
            return 1.5        
        elif rotaObjto == "BS":
            return 1.2
        elif rotaObjto == "RB":
            return 1.5
        elif rotaObjto == "SR":
            return 1
        elif rotaObjto == "RS":
            return 1
        elif rotaObjto == "SB" :
            return 1.2
        else:
            print("a Rota não foi encontrada, verifique a ortografia e tente novamente.")
            continue
#--------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------- interface do programa


nome= input("Digite seu nome:")
print("="* 45)
print(f"Seja muito bem-vindo {nome}, a Transportadora 'CHEGA RAPIDO!!!' ") 
print("Desenvolvido por: Vinicius Falcão RU: 4045314")
print("="* 45)
#---------------------------------------------------------------------------------------------


#--------------------------------------------- definindo variaveis que recebem as funções criadas anteriormente e aplicando o total com a multiplicação de ambas

dimensoes4045314 = dimObj()
peso4045314 = pesoObj()
rota4045314 = rotaObj()

total4045314 = dimensoes4045314*peso4045314*rota4045314
#---------------------------------------------------------------------------------------------

print('Valor final é de: R$ {:.2f} | (Dimensões: {} * peso: {} * rota: {})'.format(total4045314,dimensoes4045314,peso4045314,rota4045314))
           
            