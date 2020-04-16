
import math

co=float(input('Valor do cateto oposto: '))
ca=float(input('Digite o cateto adjacente'))
hip=math.sqrt(math.pow(co,2)+math.pow(ca,2))
seno=co/hip
coseno=ca/hip
tangente = co/ca

print('seno = {} \n coseno = {} \n tangente = {} '.format(seno,coseno,tangente))