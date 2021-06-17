#1. Básico : imprime todos los enteros del 0 al 150.
for i in range (151):
    print (i)

#2. Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for i in range (1001,5):
    print (i)

#3. Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for i in range (1,101):
    if i % 10 == 0:
        print ("Coding Dojo")
    elif i % 5 == 0:
        print ("Coding")
    else :   
        print (i)

#4. ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
sumImpares = 0
for i in range (500001):
    if i%2==1:
        sumImpares += i
print (sumImpares)

#5. Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range (2018,0,-4):
    if i > 0 :
        print (i)

#6. Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 0
highNum = 0
mult = 0
lowNum = int(input ("Ingrese un número:  "))
highNum = int(input ("Ingrese otro número:  "))
mult = int(input ("Ingrese un múltiplo:  "))
for i in range (lowNum, (highNum+1)):
    if i%mult==0:
        print (i)

#BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?
print (2)
print (3)
print (5)
print (7)
for i in range (8,1000):
    if (i%2!=0) and (i%3!=0) and (i%5!=0) and (i%7!=0):
        print (i)