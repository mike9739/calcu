import math
def Suma(a,b):
    return a+b

def Resta(a,b):
    return a-b

def Division(a,b):
    return (a/b)

def Multiplicacion(a,b):
    return (a*b)

def raiz(a,b):
	##Se saca la raiz con la funcion sqrt
	raizz=math.sqrt(a)
	raizz2=math.sqrt(b)
	return raizz,raizz2


def menu():
    print('\tCalculadora')
    print('1.-Suma')
    print('2.-Resta')
    print('3.-Division')
    print('4.-Multiplicacion')
    print('5.-Raiz')

    opc = int(input("Selecione Opcion:"))

    while(opc>0 and opc <5):
        x=int(input('Ingrese el primer numero:'))
        y=int(input('\nIngrese el segundo numero:'))

        if(opc ==1):
            print('La suma es:',Suma(x,y))
            break
        elif(opc ==2):
            print('La resta es:',Resta(x,y))
            break
        elif(opc ==3):
            print('La Division es:',Division(x,y))
            break
        elif(opc ==4):
            print('La Multiplicacion es:',Multiplicacion(x,y))
            break
        elif(opc ==5):
            print('La Raiz es:',raiz(x,y))
            break
menu()

