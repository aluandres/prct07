#!/usr/bin/python 
#!encoding: UTF-8
import modulo
#PRograma principal 
tuplas = (10,20, 30, 40) #declaracion de variables
lista = []
for i in tuplas:
  valor_pi = modulo.calcular_pi (i)
  lista.append (valor_pi)
print lista

pi35 = []
for i in tuplas:
  pi35.append (modulo.PI35DT)
dif35 = []
for i in range (len (tuplas)):
  dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista a"
for i in range (len (tuplas)):
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,pi35[i], lista[i], dif35[i])

#Para saber mas...
print "Pasando la salida a una matriz...."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #
matriz = []
for i in range (len (tuplas)):
  matriz.append([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len (tuplas)):
    print
    print matriz[i][0], #
    for j in range (1,4):
      print "\t%1.10f" % matriz[i][j], #
  

    
  