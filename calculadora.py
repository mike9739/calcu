def Suma(a,b):
    return a+b

def Resta(a,b):
    return a-b

def Division(a,b):
    return (a/b)

def Multiplicacion(a,b):
    return (a*b)

def raiz():
    pass
<<<<<<< HEAD
=======


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
        elif(opc ==2):
            print('La resta es:',Resta(x,y))
        elif(opc ==3):
            print('La Division es:',Division(x,y))
        elif(opc ==4):
            print('La Multiplicacion es:',Multiplicacion(x,y))
        elif(opc ==5):
            print('La Raiz es:',Raiz(x,y))
menu()
>>>>>>> e45850b2d8dcfba844e87071e60549e920bea00d
