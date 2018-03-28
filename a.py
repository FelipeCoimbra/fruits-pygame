#lista de exercicios1
#questão 1 area do retangulo
def arearet(x,y):
    return x*y
#questão 2 area da coroa circular
from math import pi
def areacoroa(x,y):
    return pi*x**2-pi*y**2
#questão 3 resto da divisão
def resto(a,b):
    return int(a/b), a%b



#questao 4 ordenada da função
def funcao(a,b,c,x):
    y=a*x**2+b*x+c
    return x,y

#questao 5 gorjeta do garcom
def gorj(x):
    return x*0.1

#questao 6 media dos numeros
def media(x,y):
    return (x+y)/2

#questao 7 media ponderada
def mediap(x,y,p1,p2):
    return (x*p1+y*p2)/(p1+p2)

#questao 8 distancia de arrasto da correnteza
def distc(x,y,z):
    #x(largura da correnteza,y(velocidade da correnteza, z(vel do barco)
    return y*x/z


#questao 9 saldo final da conta
def saldoconta(x,y,z):
    #x(saldo inicial),y(numero de meses), z(taxa de juros)
    return x*(1+y*z)


#questao 10 calculo do erro
def erro(q,n):
    return (1/(1-q))-(q ** n - 1)/(q - 1)

#questao 11 calculo do tempo de prova do corredor
def tempo(si,mi,hi,sf,mf,hf):
    #t0 = 3600 * si + 60 * mi * hi, tf = 3600 * sf + 60 mf + hf
    return 
 






#questao 12 calcular o valor da gorjeta
def gorjtotal(x,y):
    #lembrando que x é o valor da conta e y é o numero de pessoas
    return 1.1*x/y


#questao 13 cacular a area da superficie do cubo
def areacubo(x):
    #x é a aresta do cubo
    return 6*x**2
